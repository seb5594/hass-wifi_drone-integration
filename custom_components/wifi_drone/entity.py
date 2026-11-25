"""Device and entity metadata shared by WiFi Drone platforms."""

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import DroneConfigEntry, DroneCoordinator
from .const import DOMAIN


class DroneEntity(CoordinatorEntity[DroneCoordinator]):
    """An entity belonging to the configured bridge."""

    _attr_has_entity_name = True

    def __init__(self, entry: DroneConfigEntry, key: str) -> None:
        super().__init__(entry.runtime_data)
        self._attr_unique_id = f"{entry.entry_id}_{key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)}, name=entry.title, model="WiFi Drone Bridge"
        )
