from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "My API"
    SECRET_KEY: str = "super-secret"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "mydb"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    API_V1_STR: str = "/api/v1"

    # Pydantic v2 style config
    model_config = SettingsConfigDict(
        env_file=".env",  # load variables from .env if provided at runtime
        extra="ignore",   # silently ignore unknown env vars
    )


settings = Settings()
