"""MODELS - COMMON
Common variables and base classes for the models
"""

# # Installed # #
from pydantic import BaseModel as PydanticBaseModel, model_validator, ConfigDict

__all__ = ("BaseModel",)


class BaseModel(PydanticBaseModel):
    """All data models inherit from this class"""

    @model_validator(mode="before")
    @classmethod
    def _min_properties(cls, data):
        """At least one property is required"""
        if not data:
            raise ValueError("At least one property is required")
        return data

    def model_dump(self, include_nulls=False, **kwargs):
        """Override the super dict method by removing null keys from the dict, unless include_nulls=True"""
        kwargs["exclude_none"] = not include_nulls
        return super().model_dump(**kwargs)

    model_config = ConfigDict(
        extra="forbid",  # forbid sending additional fields/properties
        anystr_strip_whitespace=True,  # strip whitespaces from strings
    )

