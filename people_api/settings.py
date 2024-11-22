from __future__ import annotations

from pydantic import BaseSettings, Field

__all__ = ("api_settings", "mongo_settings")


class BaseSettings(BaseSettings):
    class Config:
        env_file = ".env"


class APISettings(BaseSettings):
    title: str = Field("People API", env="API_TITLE")
    host: str = Field("0.0.0.0", env="API_HOST")
    port: int = Field(5000, env="API_PORT")
    log_level: str = Field("INFO", env="API_LOG_LEVEL")


class MongoSettings(BaseSettings):
    uri: str = Field("mongodb://127.0.0.1:27017", env="MONGO_URI")
    database: str = Field("fastapi+pydantic+mongo-example", env="MONGO_DATABASE")
    collection: str = Field("people", env="MONGO_COLLECTION")


api_settings = APISettings()
mongo_settings = MongoSettings()
