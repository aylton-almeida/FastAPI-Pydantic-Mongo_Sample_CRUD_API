"""SETTINGS
Settings loaders using Pydantic BaseSettings classes (load from environment variables / dotenv file)
"""

# # Installed # #
from pydantic_settings import BaseSettings
from pydantic import Field

__all__ = ("api_settings", "mongo_settings")


class CustomBaseSettings(BaseSettings):
    class Config:
        env_file = ".env"


class APISettings(CustomBaseSettings):
    title: str = Field(default="People API")
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=5000)
    log_level: str = Field(default="INFO")

    class Config(CustomBaseSettings.Config):
        env_prefix = "API_"


class MongoSettings(CustomBaseSettings):
    uri: str = Field(default="mongodb://127.0.0.1:27017")
    database: str = Field(default="fastapi+pydantic+mongo-example")
    collection: str = Field(default="people")

    class Config(CustomBaseSettings.Config):
        env_prefix = "MONGO_"


api_settings = APISettings()
mongo_settings = MongoSettings()

