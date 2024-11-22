"""MODELS - PERSON - CREATE
Person Create model. Inherits from PersonUpdate, but all the required fields must be re-defined
"""

# # Package # #
from .person_update import PersonUpdate
from .person_address import Address
from .fields import PersonFields
from pydantic import BaseModel, Field

__all__ = ("PersonCreate",)


class PersonCreate(PersonUpdate):
    """Body of Person POST requests"""
    name: str = Field(..., description=PersonFields.name)
    address: Address = Field(..., description=PersonFields.address)
    # Birth remains Optional, so is not required to re-declare

