from typing import Optional, Any

from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict


class DbConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

    POSTGRES_SERVER: Optional[str] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_DB: Optional[str] = None
    SQLALCHEMY_DATABASE_URI: PostgresDsn | str | None = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], values: ValidationInfo) -> Any:
        """Pydantic's validator requires @classmethod rather than @staticmethod for cls.fields access"""
        print(v)
        if isinstance(v, str):
            print("Loading SQLALCHEMY_DATABASE_URI from .env file ...")
            return v
        print("Creating SQLALCHEMY_DATABASE_URI from .env file ...")
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_SERVER"),
            path=f"{values.data.get('POSTGRES_DB') or ''}",
        )


CONFIG = DbConfig()
