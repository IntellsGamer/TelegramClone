from fastapi import Request

from app.core.feature_manager import FeatureManager
from app.core.settings import Settings
from app.services.environment import EnvironmentDetector


def make_settings(**overrides):
    base = {
        "DATABASE_URL": "postgresql+asyncpg://postgres:postgres@localhost:5432/test",
        "REDIS_URL": "redis://localhost:6379/0",
    }
    base.update(overrides)
    return Settings(**base)


def test_feature_matrix_reflects_toggles():
    settings = make_settings(ENABLE_VOICE_MESSAGES=False)
    manager = FeatureManager(settings)
    assert manager.enabled("voice_messages") is False
    assert manager.enabled("file_attachments") is True


def test_protocol_detection_prefers_forwarded_proto():
    settings = make_settings(TRUST_PROXY_HEADERS=True)
    detector = EnvironmentDetector(settings)

    scope = {
        "type": "http",
        "method": "GET",
        "headers": [(b"x-forwarded-proto", b"https")],
        "scheme": "http",
        "path": "/api/health",
        "query_string": b"",
        "server": ("localhost", 8000),
        "client": ("127.0.0.1", 12345),
    }
    request = Request(scope)

    info = detector.detect(request)
    assert info.protocol == "https"
    assert info.websocket_protocol == "wss"
