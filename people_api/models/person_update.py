from __future__ import annotations

from datetime import date
from typing import Optional
from contextlib import suppress

from pydantic import BaseModel, Field, model_validator

from .person_address import Address


class PersonFields:
    name: Optional[str] = Field(None, description="The name of the person")
    address_update: Optional[Address] = Field(None, description="The address of the person")
    birth: Optional[date] = Field(None, description="The birth date of the person")


class PersonUpdate(BaseModel):
    """Body of Person PATCH requests"""
    name: Optional[str] = PersonFields.name
    address: Optional[Address] = PersonFields.address_update
    birth: Optional[date] = PersonFields.birth

    @model_validator(mode="before")
    @classmethod
    def _convert_birth_to_string(cls, data) -> PersonUpdate:
        """Converts the "birth" field to string (isoformat) when exporting to dict (for Mongo)"""
        if "birth" in data:
            data["birth"] = data["birth"].isoformat()
        return data

    model_config = {"extra": "ignore"}

