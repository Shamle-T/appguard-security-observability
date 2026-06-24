"""Application configuration placeholder."""

# Used for central settings/config fie for FastAPI backend

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AppGuard"
    app_version: str = "0.1.0"
    environment: str = "development"
    api_v1_prefix: str = "/api/v1"

    database_url: str = (
        "postgresql+psycopg://appguard:appguard_password@localhost:5432/appguard_db"
    )

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
