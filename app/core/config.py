from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Fable"
    SECRET_KEY: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    API_V1_STR: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=None,
        extra="ignore",
    )

settings = Settings()
