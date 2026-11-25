"""Set up the WiFi Drone integration."""

from datetime import timedelta
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import BridgeClient, BridgeError, InvalidAuth
from .const import CONF_API_TOKEN, CONF_BRIDGE_URL, DOMAIN

PLATFORMS = [Platform.CAMERA, Platform.BINARY_SENSOR]
_LOGGER = logging.getLogger(__name__)


class DroneCoordinator(DataUpdateCoordinator[str]):
    """Track the bridge and stream availability."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        super().__init__(
            hass, _LOGGER, name=DOMAIN, update_interval=timedelta(seconds=10),
            config_entry=entry, always_update=False,
        )
        self.client = BridgeClient(
            async_get_clientsession(hass), entry.data[CONF_BRIDGE_URL], entry.data[CONF_API_TOKEN]
        )

    async def _async_update_data(self) -> str:
        try:
            return await self.client.status()
        except InvalidAuth as error:
            raise ConfigEntryAuthFailed("The bridge rejected the API token") from error
        except BridgeError as error:
            raise UpdateFailed("Could not read bridge status") from error


type DroneConfigEntry = ConfigEntry[DroneCoordinator]


async def async_setup_entry(hass: HomeAssistant, entry: DroneConfigEntry) -> bool:
    coordinator = DroneCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: DroneConfigEntry) -> bool:
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
