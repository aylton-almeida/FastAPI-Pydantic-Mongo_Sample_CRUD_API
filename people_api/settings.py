"""SETTINGS
Settings loaders using Pydantic BaseSettings classes (load from environment variables / dotenv file)
"""

# # Installed # #
from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings

__all__ = ("api_settings", "mongo_settings")


class BaseSettings(BaseSettings):
    model_config = {"env_file": ".env"}


class APISettings(BaseSettings):
    title: str = Field(default="People API")
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=5000)
    log_level: str = Field(default="INFO")

    model_config = {"env_prefix": "API_"}


class MongoSettings(BaseSettings):
    uri: str = Field(default="mongodb://127.0.0.1:27017")
    database: str = Field(default="fastapi+pydantic+mongo-example")
    collection: str = Field(default="people")

    model_config = {"env_prefix": "MONGO_"}


api_settings = APISettings()
mongo_settings = MongoSettings()

