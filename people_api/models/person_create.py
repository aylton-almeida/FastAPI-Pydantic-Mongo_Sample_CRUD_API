from typing import Optional
from pydantic import BaseModel, Field, model_validator
from .person_address import Address
from .fields import PersonFields

class PersonUpdate(BaseModel):
    name: Optional[str] = PersonFields.name
    address: Optional[Address] = PersonFields.address

    model_config = {"extra": "ignore"}

class PersonCreate(PersonUpdate):
    """Body of Person POST requests"""
    name: str = PersonFields.name
    address: Address = PersonFields.address
    # Birth remains Optional, so is not required to re-declare

    model_config = {"extra": "ignore"}

