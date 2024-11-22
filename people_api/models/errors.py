from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("BaseError", "BaseIdentifiedError", "NotFoundError", "AlreadyExistsError")


class BaseError(BaseModel):
    message: str = Field(..., description="Error message or description")

    model_config = {"extra": "ignore"}


class BaseIdentifiedError(BaseError):
    identifier: str = Field(..., description="Unique identifier which this error references to")

    model_config = {"extra": "ignore"}


class NotFoundError(BaseIdentifiedError):
    """The entity does not exist"""
    model_config = {"extra": "ignore"}


class AlreadyExistsError(BaseIdentifiedError):
    """An entity being created already exists"""
    model_config = {"extra": "ignore"}

