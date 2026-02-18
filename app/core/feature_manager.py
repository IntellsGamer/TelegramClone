from dataclasses import dataclass

from app.core.settings import Settings


@dataclass(frozen=True)
class FeatureState:
    name: str
    enabled: bool
    description: str


class FeatureManager:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._features = {
            "email_verification": FeatureState("email_verification", settings.enable_email_verification, "Require email verification during signup"),
            "file_attachments": FeatureState("file_attachments", settings.enable_file_attachments, "Allow upload and sharing files"),
            "voice_messages": FeatureState("voice_messages", settings.enable_voice_messages, "Voice message recording and playback"),
            "video_calls": FeatureState("video_calls", settings.enable_video_calls, "Experimental video calls"),
            "bot_framework": FeatureState("bot_framework", settings.enable_bot_framework, "Bot API compatibility layer"),
            "encryption": FeatureState("encryption", settings.enable_encryption, "E2E and secret chat feature family"),
            "public_channels": FeatureState("public_channels", settings.enable_public_channels, "Public groups/channel discovery"),
            "stories": FeatureState("stories", settings.enable_stories, "Story timeline and publishing"),
        }

    def enabled(self, feature_name: str) -> bool:
        feature = self._features.get(feature_name)
        return bool(feature and feature.enabled)

    def matrix(self) -> list[FeatureState]:
        return list(self._features.values())
