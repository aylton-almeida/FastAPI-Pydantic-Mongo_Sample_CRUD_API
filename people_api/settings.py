from __future__ import annotations

import pydantic
from pydantic import BaseSettings, Field

__all__ = ("api_settings", "mongo_settings")


class BaseSettings(BaseSettings):
    model_config = {"env_file": ".env"}


class APISettings(BaseSettings):
    title: str = Field("People API")
    host: str = Field("0.0.0.0")
    port: int = Field(5000)
    log_level: str = Field("INFO")

    model_config = {"env_prefix": "API_"}


class MongoSettings(BaseSettings):
    uri: str = Field("mongodb://127.0.0.1:27017")
    database: str = Field("fastapi+pydantic+mongo-example")
    collection: str = Field("people")

    model_config = {"env_prefix": "MONGO_"}


api_settings: APISettings = APISettings()
mongo_settings: MongoSettings = MongoSettings()
