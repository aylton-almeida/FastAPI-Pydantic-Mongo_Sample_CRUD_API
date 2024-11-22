"""MODELS - COMMON
Common variables and base classes for the models
"""

# # Installed # #
from __future__ import annotations

from pydantic import BaseModel as PydanticBaseModel, Extra, model_validator
from typing import Any

__all__ = ("BaseModel",)


class BaseModel(PydanticBaseModel):
    """All data models inherit from this class"""

    @model_validator(mode="before")
    @classmethod
    def _min_properties(cls, data: dict[str, Any]) -> dict[str, Any]:
        """At least one property is required"""
        if not data:
            raise ValueError("At least one property is required")
        return data

    def dict(self, include_nulls: bool = False, **kwargs: Any) -> dict[str, Any]:
        """Override the super dict method by removing null keys from the dict, unless include_nulls=True"""
        kwargs["exclude_none"] = not include_nulls
        return super().dict(**kwargs)

    model_config = {
        "extra": Extra.forbid,  # forbid sending additional fields/properties
        "anystr_strip_whitespace": True,  # strip whitespaces from strings
    }

