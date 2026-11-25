"""Config entry lifecycle against a real Home Assistant Core."""

from importlib import import_module
from pathlib import Path

import pytest

pytest.importorskip("pytest_homeassistant_custom_component")

from homeassistant.config_entries import ConfigEntryState  # noqa: E402
from homeassistant.setup import async_setup_component  # noqa: E402
from pytest_homeassistant_custom_component.common import MockConfigEntry  # noqa: E402

DOMAIN = "wifi_drone"
URL = "http://drone-bridge.local:8099"
TOKEN = "test-token-for-ha-123"
DATA = {"bridge_url": URL, "api_token": TOKEN}
STATUS_URL = f"{URL}/api/v1/status"


@pytest.fixture(autouse=True)
def enable_wifi_drone(hass, enable_custom_integrations, monkeypatch):
    root = Path(__file__).resolve().parents[2]
    monkeypatch.syspath_prepend(str(root))
    namespace = import_module("custom_components")
    folder = str(root / "custom_components")
    if folder not in namespace.__path__:
        namespace.__path__.append(folder)
    # The shared runner marks manifest dependencies loaded. These tests use real entities.
    hass.config.components.difference_update({"camera", "binary_sensor"})
    yield


async def test_user_flow_rejects_wrong_token_and_duplicate_bridge(hass, aioclient_mock):
    initial = await hass.config_entries.flow.async_init(DOMAIN, context={"source": "user"})
    assert initial["type"] == "form"

    aioclient_mock.get(STATUS_URL, status=401)
    denied = await hass.config_entries.flow.async_configure(initial["flow_id"], DATA)
    assert denied["errors"] == {"base": "invalid_auth"}

    aioclient_mock.clear_requests()
    aioclient_mock.get(STATUS_URL, json={"api_version": 1, "state": "streaming"})
    result = await hass.config_entries.flow.async_configure(initial["flow_id"], DATA)
    assert result["type"] == "create_entry"
    await hass.async_block_till_done()

    flow = await hass.config_entries.flow.async_init(DOMAIN, context={"source": "user"})
    duplicate = await hass.config_entries.flow.async_configure(flow["flow_id"], DATA)
    assert duplicate["type"] == "abort"
    assert duplicate["reason"] == "already_configured"


async def test_entry_loads_and_unloads_entities(hass, aioclient_mock):
    assert await async_setup_component(hass, "homeassistant", {})
    aioclient_mock.get(STATUS_URL, json={"api_version": 1, "state": "streaming"})
    entry = MockConfigEntry(domain=DOMAIN, title="WiFi Drone", data=DATA)
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    assert entry.state is ConfigEntryState.LOADED
    assert hass.states.get("camera.wifi_drone").state == "idle"
    assert hass.states.get("binary_sensor.wifi_drone_video_stream").state == "on"
    assert await hass.config_entries.async_unload(entry.entry_id)
    assert entry.state is ConfigEntryState.NOT_LOADED
