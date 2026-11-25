"""JPEG snapshots and MJPEG from the WiFi Drone Bridge."""

import asyncio
from contextlib import suppress

from aiohttp import ClientError, web
from homeassistant.components.camera import Camera
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DroneConfigEntry
from .entity import DroneEntity


async def async_setup_entry(
    hass: HomeAssistant, entry: DroneConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    async_add_entities([DroneCamera(entry)])


class DroneCamera(DroneEntity, Camera):
    """A camera backed by the bridge's MJPEG endpoint."""

    _attr_name = None

    def __init__(self, entry: DroneConfigEntry) -> None:
        super().__init__(entry, "camera")
        Camera.__init__(self)

    @property
    def available(self) -> bool:
        return super().available and self.coordinator.data == "streaming"

    async def async_camera_image(
        self, width: int | None = None, height: int | None = None
    ) -> bytes | None:
        with suppress(ClientError, TimeoutError):
            return await self.coordinator.client.snapshot()
        return None

    async def handle_async_mjpeg_stream(self, request: web.Request) -> web.StreamResponse:
        downstream = None
        try:
            async with self.coordinator.client.get("stream.mjpg", streaming=True) as upstream:
                content_type = upstream.headers.get("Content-Type", "")
                if upstream.status != 200 or upstream.content_type != "multipart/x-mixed-replace":
                    raise web.HTTPServiceUnavailable()
                downstream = web.StreamResponse(
                    headers={"Content-Type": content_type, "Cache-Control": "no-store"}
                )
                await downstream.prepare(request)
                async for chunk in upstream.content.iter_chunked(32 * 1024):
                    async with asyncio.timeout(5):
                        await downstream.write(chunk)
        except (ClientError, ConnectionError, TimeoutError):
            if downstream is None:
                raise web.HTTPServiceUnavailable() from None
        return downstream
