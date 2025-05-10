from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "My API"
    SECRET_KEY = os.getenv("SECRET_KEY", "default-key")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_NAME = os.getenv("DB_NAME", "mydb")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    API_V1_STR: str = "/api/v1"

    # Pydantic v2 style config
    model_config = SettingsConfigDict(
        extra="ignore",   # silently ignore unknown env vars
    )


settings = Settings()
