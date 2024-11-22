from __future__ import annotations

from pydantic import BaseModel, Field

class AddressFields:
    street: str = Field(..., description="Street name and number")
    city: str = Field(..., description="City name")
    state: str = Field(..., description="State name")
    zip_code: str = Field(..., description="Zip code")

class Address(BaseModel):
    """The address information of a person"""
    street: str = AddressFields.street
    city: str = AddressFields.city
    state: str = AddressFields.state
    zip_code: str = AddressFields.zip_code

    class Config:
        extra = "ignore"
