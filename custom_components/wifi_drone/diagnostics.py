"""Diagnostic data for the configured bridge."""

from homeassistant.core import HomeAssistant

from . import DroneConfigEntry


async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: DroneConfigEntry):
    coordinator = entry.runtime_data
    return {
        "bridge_available": coordinator.last_update_success,
        "stream_state": coordinator.data,
    }
