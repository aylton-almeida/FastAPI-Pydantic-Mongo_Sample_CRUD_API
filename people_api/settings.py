"""SETTINGS
Settings loaders using Pydantic BaseSettings classes (load from environment variables / dotenv file)
"""

# # Installed # #
import pydantic
from typing import Optional

__all__ = ("api_settings", "mongo_settings")


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class APISettings(BaseSettings):
    title: str = "People API"
    host: str = "0.0.0.0"
    port: int = 5000
    log_level: str = "INFO"

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class MongoSettings(BaseSettings):
    uri: str = "mongodb://127.0.0.1:27017"
    database: str = "fastapi+pydantic+mongo-example"
    collection: str = "people"

    class Config(BaseSettings.Config):
        env_prefix = "MONGO_"


api_settings: Optional[APISettings] = None
mongo_settings: Optional[MongoSettings] = None

async def load_settings():
    global api_settings, mongo_settings
    api_settings = APISettings()
    mongo_settings = MongoSettings()

