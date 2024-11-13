"""SETTINGS
Settings loaders using Pydantic BaseSettings classes (load from environment variables / dotenv file)
"""

# # Installed # #
import pydantic
from pydantic import ConfigDict

__all__ = ("api_settings", "mongo_settings")


class BaseSettings(pydantic.BaseSettings):
    model_config = ConfigDict(env_file=".env")


class APISettings(BaseSettings):
    title: str = "People API"
    host: str = "0.0.0.0"
    port: int = 5000
    log_level: str = "INFO"

    # TODO[pydantic]: The `Config` class inherits from another class, please create the `model_config` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    class Config(BaseSettings.Config):
        env_prefix = "API_"


class MongoSettings(BaseSettings):
    uri: str = "mongodb://127.0.0.1:27017"
    database: str = "fastapi+pydantic+mongo-example"
    collection: str = "people"

    # TODO[pydantic]: The `Config` class inherits from another class, please create the `model_config` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    class Config(BaseSettings.Config):
        env_prefix = "MONGO_"


api_settings = APISettings()
mongo_settings = MongoSettings()
