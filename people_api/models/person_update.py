from __future__ import annotations

from datetime import date
from typing import Optional
from contextlib import suppress

from pydantic import BaseModel, Field

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

    class Config:
        extra = "ignore"
        json_encoders = {
            date: lambda v: v.isoformat(),
        }

    def dict(self, **kwargs):
        # The "birth" field must be converted to string (isoformat) when exporting to dict (for Mongo)
        # TODO Better way to do this? (automatic conversion can be done with Config.json_encoders, but not available for dict
        d = super().dict(**kwargs)
        with suppress(KeyError):
            d["birth"] = d.pop("birth").isoformat()
        return d
