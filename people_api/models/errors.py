"""MODELS - ERRORS
Models for Error responses. Custom exceptions must be associated with one of these
"""

# # Installed # #
from pydantic import BaseModel, Field
from typing import Annotated

__all__ = ("BaseError", "BaseIdentifiedError", "NotFoundError", "AlreadyExistsError")


class BaseError(BaseModel):
    message: Annotated[str, Field(description="Error message or description")]


class BaseIdentifiedError(BaseError):
    identifier: Annotated[str, Field(description="Unique identifier which this error references to")]


class NotFoundError(BaseIdentifiedError):
    """The entity does not exist"""
    pass


class AlreadyExistsError(BaseIdentifiedError):
    """An entity being created already exists"""
    pass

