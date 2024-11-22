from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional

__all__ = ("BaseError", "BaseIdentifiedError", "NotFoundError", "AlreadyExistsError")


class BaseError(BaseModel):
    message: str = Field(..., description="Error message or description")

    class Config:
        extra = "ignore"


class BaseIdentifiedError(BaseError):
    identifier: str = Field(..., description="Unique identifier which this error references to")


class NotFoundError(BaseIdentifiedError):
    """The entity does not exist"""
    pass


class AlreadyExistsError(BaseIdentifiedError):
    """An entity being created already exists"""
    pass
