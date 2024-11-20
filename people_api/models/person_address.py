"""MODELS - PERSON ADDRESS
The address of a person is part of the Person model
"""

# # Package # #
from .common import BaseModel
from .fields import AddressFields
from typing import Optional

__all__ = ("Address",)


class Address(BaseModel):
    """The address information of a person"""
    street: Optional[str] = AddressFields.street
    city: Optional[str] = AddressFields.city
    state: Optional[str] = AddressFields.state
    zip_code: Optional[str] = AddressFields.zip_code

