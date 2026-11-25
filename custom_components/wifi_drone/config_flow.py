"""UI configuration for a WiFi Drone Bridge."""

import voluptuous as vol
from yarl import URL

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.selector import TextSelector, TextSelectorConfig, TextSelectorType

from .api import BridgeClient, BridgeError, InvalidAuth, bridge_url
from .const import CONF_API_TOKEN, CONF_BRIDGE_URL, DEFAULT_URL, DOMAIN


class WiFiDroneConfigFlow(ConfigFlow, domain=DOMAIN):
    """Connect to a bridge and allow later edits."""

    VERSION = 1

    async def async_step_user(self, user_input=None) -> ConfigFlowResult:
        return await self._form("user", user_input)

    async def async_step_reconfigure(self, user_input=None) -> ConfigFlowResult:
        return await self._form("reconfigure", user_input)

    async def async_step_reauth(self, entry_data) -> ConfigFlowResult:
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(self, user_input=None) -> ConfigFlowResult:
        return await self._form("reauth_confirm", user_input)

    async def _form(self, step: str, user_input) -> ConfigFlowResult:
        entry = None
        if step == "reconfigure":
            entry = self._get_reconfigure_entry()
        elif step == "reauth_confirm":
            entry = self._get_reauth_entry()
        default_url = entry.data[CONF_BRIDGE_URL] if entry else DEFAULT_URL
        errors = {}
        if user_input is not None:
            default_url = user_input.get(CONF_BRIDGE_URL, default_url)
            token = user_input[CONF_API_TOKEN].strip()
            try:
                url = bridge_url(default_url)
            except ValueError:
                errors[CONF_BRIDGE_URL] = "invalid_url"
            else:
                client = BridgeClient(async_get_clientsession(self.hass), url, token)
                try:
                    await client.status()
                except InvalidAuth:
                    errors["base"] = "invalid_auth"
                except BridgeError:
                    errors["base"] = "cannot_connect"
                else:
                    if any(
                        other is not entry and other.data.get(CONF_BRIDGE_URL) == url
                        for other in self._async_current_entries()
                    ):
                        return self.async_abort(reason="already_configured")
                    data = {CONF_BRIDGE_URL: url, CONF_API_TOKEN: token}
                    title = f"WiFi Drone ({URL(url).host})"
                    if entry is not None:
                        return self.async_update_reload_and_abort(entry, title=title, data=data)
                    return self.async_create_entry(title=title, data=data)

        fields = {}
        if step != "reauth_confirm":
            fields[vol.Required(CONF_BRIDGE_URL, default=default_url)] = TextSelector()
        fields[vol.Required(CONF_API_TOKEN)] = TextSelector(
            TextSelectorConfig(type=TextSelectorType.PASSWORD)
        )
        return self.async_show_form(step_id=step, data_schema=vol.Schema(fields), errors=errors)
