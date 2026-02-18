from dataclasses import dataclass

from fastapi import Request

from app.core.settings import Settings


@dataclass
class ProtocolInfo:
    protocol: str
    websocket_protocol: str
    via_proxy: bool


class EnvironmentDetector:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def detect(self, request: Request) -> ProtocolInfo:
        forwarded_proto = request.headers.get("x-forwarded-proto") if self.settings.trust_proxy_headers else None
        protocol = forwarded_proto or request.url.scheme

        if self.settings.force_https:
            protocol = "https"

        websocket_protocol = "wss" if protocol == "https" else "ws"
        return ProtocolInfo(protocol=protocol, websocket_protocol=websocket_protocol, via_proxy=bool(forwarded_proto))
