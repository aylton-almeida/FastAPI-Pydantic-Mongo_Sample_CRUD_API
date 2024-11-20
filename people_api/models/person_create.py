"""MODELS - PERSON - CREATE
Person Create model. Inherits from PersonUpdate, but all the required fields must be re-defined
"""

# # Package # #
from .person_update import PersonUpdate
from .person_address import Address
from .fields import PersonFields
from typing import Optional

__all__ = ("PersonCreate",)


class PersonCreate(PersonUpdate):
    """Body of Person POST requests"""
    name: str = PersonFields.name
    address: Address = PersonFields.address
    birth: Optional[str] = PersonFields.birth

