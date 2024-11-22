from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel as PydanticBaseModel, Extra, root_validator


class BaseModel(PydanticBaseModel):
    """All data models inherit from this class"""

    @root_validator(pre=True)
    def _min_properties(cls, data: Dict[str, Any]) -> Dict[str, Any]:
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
