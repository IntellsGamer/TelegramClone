from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = Field(default="Telegram Web Clone (Python)", alias="APP_NAME")
    env: str = Field(default="development", alias="ENV")
    secret_key: str = Field(default="change-me", alias="SECRET_KEY")
    access_token_expire_minutes: int = Field(default=120, alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    database_url: str = Field(default="postgresql+asyncpg://postgres:postgres@localhost:5432/telegram_clone", alias="DATABASE_URL")
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")
    storage_path: str = Field(default="./storage", alias="STORAGE_PATH")

    enable_email_verification: bool = Field(default=False, alias="ENABLE_EMAIL_VERIFICATION")
    enable_phone_registration: bool = Field(default=False, alias="ENABLE_PHONE_REGISTRATION")
    enable_file_attachments: bool = Field(default=True, alias="ENABLE_FILE_ATTACHMENTS")
    enable_voice_messages: bool = Field(default=True, alias="ENABLE_VOICE_MESSAGES")
    enable_video_calls: bool = Field(default=False, alias="ENABLE_VIDEO_CALLS")
    enable_bot_framework: bool = Field(default=True, alias="ENABLE_BOT_FRAMEWORK")
    enable_encryption: bool = Field(default=True, alias="ENABLE_ENCRYPTION")
    enable_public_channels: bool = Field(default=True, alias="ENABLE_PUBLIC_CHANNELS")
    enable_stories: bool = Field(default=False, alias="ENABLE_STORIES")

    use_s3_storage: bool = Field(default=False, alias="USE_S3_STORAGE")
    use_cdn: bool = Field(default=False, alias="USE_CDN")
    enable_rate_limiting: bool = Field(default=True, alias="ENABLE_RATE_LIMITING")
    enable_audit_log: bool = Field(default=True, alias="ENABLE_AUDIT_LOG")

    trust_proxy_headers: bool = Field(default=True, alias="TRUST_PROXY_HEADERS")
    force_https: bool = Field(default=False, alias="FORCE_HTTPS")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
