"""MODELS - COMMON
Common variables and base classes for the models
"""

# # Installed # #
from pydantic import BaseModel as PydanticBaseModel, root_validator, Extra
from typing import Any, Dict

__all__ = ("BaseModel",)


class BaseModel(PydanticBaseModel):
    """All data models inherit from this class"""

    @root_validator(pre=True)
    def _min_properties(cls: Any, data: Dict[str, Any]) -> Dict[str, Any]:
        """At least one property is required"""
        if not data:
            raise ValueError("At least one property is required")
        return data

    def dict(self, include_nulls: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Override the super dict method by removing null keys from the dict, unless include_nulls=True"""
        kwargs["exclude_none"] = not include_nulls
        return super().dict(**kwargs)

    class Config:
        extra = Extra.forbid  # forbid sending additional fields/properties
        anystr_strip_whitespace = True  # strip whitespaces from strings

