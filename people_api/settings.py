"""SETTINGS
Settings loaders using Pydantic BaseSettings classes (load from environment variables / dotenv file)
"""

# # Installed # #
from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic_settings import SettingsConfigDict

__all__ = ("api_settings", "mongo_settings")


class BaseSettings(PydanticBaseSettings):
    model_config = SettingsConfigDict(env_file=".env")


class APISettings(BaseSettings):
    title: str = "People API"
    host: str = "0.0.0.0"
    port: int = 5000
    log_level: str = "INFO"

    model_config = {"env_prefix": "API_"}


class MongoSettings(BaseSettings):
    uri: str = "mongodb://127.0.0.1:27017"
    database: str = "fastapi+pydantic+mongo-example"
    collection: str = "people"

    model_config = {"env_prefix": "MONGO_"}


api_settings = APISettings()
mongo_settings = MongoSettings()
