"""Expose whether the bridge is receiving live video."""

from homeassistant.components.binary_sensor import BinarySensorDeviceClass, BinarySensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DroneConfigEntry
from .entity import DroneEntity


async def async_setup_entry(
    hass: HomeAssistant, entry: DroneConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    async_add_entities([DroneVideoStatus(entry)])


class DroneVideoStatus(DroneEntity, BinarySensorEntity):
    """Connectivity of the drone video stream."""

    _attr_translation_key = "video_stream"
    _attr_device_class = BinarySensorDeviceClass.CONNECTIVITY

    def __init__(self, entry: DroneConfigEntry) -> None:
        super().__init__(entry, "video_stream")

    @property
    def is_on(self) -> bool:
        return self.coordinator.data == "streaming"
