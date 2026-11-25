"""Client for the WiFi Drone Bridge v1 API."""

import asyncio
from dataclasses import dataclass

from aiohttp import ClientError, ClientSession, ClientTimeout
from yarl import URL

STATES = frozenset({"unconfigured", "connecting", "streaming", "reconnecting"})


class BridgeError(Exception):
    """The bridge is unreachable or returned an invalid response."""


class InvalidAuth(BridgeError):
    """The bridge rejected the API token."""


def bridge_url(value: str) -> str:
    """Validate and normalize the bridge address."""
    url = URL(value.strip())
    if (
        url.scheme not in {"http", "https"}
        or not url.host
        or url.user is not None
        or url.password is not None
        or url.port == 0
        or url.path != "/"
        or url.query_string
        or url.fragment
    ):
        raise ValueError("Use an HTTP(S) bridge origin with no path or credentials")
    return str(url.origin())


@dataclass(slots=True)
class BridgeClient:
    session: ClientSession
    url: str
    token: str

    def get(self, path: str, *, streaming: bool = False):
        timeout = (
            ClientTimeout(total=None, connect=5, sock_read=25)
            if streaming else ClientTimeout(total=5)
        )
        return self.session.get(
            f"{self.url}/api/v1/{path}",
            headers={"Authorization": f"Bearer {self.token}"},
            timeout=timeout,
            allow_redirects=False,
        )

    async def status(self) -> str:
        try:
            async with self.get("status") as response:
                if response.status in {401, 403}:
                    raise InvalidAuth
                if response.status != 200:
                    raise BridgeError
                data = await response.json()
                if (
                    not isinstance(data, dict)
                    or data.get("api_version") != 1
                    or not isinstance(data.get("state"), str)
                    or data["state"] not in STATES
                ):
                    raise BridgeError
                return data["state"]
        except (ClientError, TimeoutError, ValueError) as error:
            raise BridgeError from error

    async def snapshot(self) -> bytes | None:
        async with self.get("snapshot.jpg") as response:
            length = response.content_length or 0
            if response.status != 200 or response.content_type != "image/jpeg":
                return None
            if not 4 <= length <= 8 * 1024 * 1024:
                return None
            try:
                return await response.content.readexactly(length)
            except asyncio.IncompleteReadError:
                return None
