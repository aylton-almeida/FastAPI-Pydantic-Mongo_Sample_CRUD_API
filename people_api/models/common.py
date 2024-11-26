"""MODELS - COMMON
Common variables and base classes for the models
"""

# # Installed # #
from pydantic import BaseModel as PydanticBaseModel, ConfigDict, RootValidator
from typing import Any, Dict, Type

__all__ = ("BaseModel",)


class BaseModel(PydanticBaseModel):
    """All data models inherit from this class"""

    @RootValidator(pre=True)
    def _min_properties(cls: Type['BaseModel'], data: Dict[str, Any]) -> Dict[str, Any]:
        """At least one property is required"""
        if not data:
            raise ValueError("At least one property is required")
        return data

    def dict(self, include_nulls: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Override the super dict method by removing null keys from the dict, unless include_nulls=True"""
        kwargs["exclude_none"] = not include_nulls
        return super().model_dump(**kwargs)

    model_config = ConfigDict(
        extra='forbid',  # forbid sending additional fields/properties
        str_strip_whitespace=True  # strip whitespaces from strings
    )

