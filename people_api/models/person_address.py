from __future__ import annotations

from pydantic import BaseModel, Field

class AddressFields:
    street: str = Field(..., description="Street of the address")
    city: str = Field(..., description="City of the address")
    state: str = Field(..., description="State of the address")
    zip_code: str = Field(..., description="Zip code of the address")

class Address(BaseModel):
    """The address information of a person"""
    street: str = AddressFields.street
    city: str = AddressFields.city
    state: str = AddressFields.state
    zip_code: str = AddressFields.zip_code

    model_config = {"extra": "ignore"}
