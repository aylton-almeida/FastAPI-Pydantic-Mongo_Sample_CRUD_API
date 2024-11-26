"""MODELS - PERSON - UPDATE
Person Update model. All attributes are set as Optional, as we use the PATCH method for update
(in which only the attributes to change are sent on request body)
"""

# # Native # #
from __future__ import annotations
from datetime import date
from typing import Optional
from contextlib import suppress

# # Package # #
from pydantic import BaseModel
from .fields import PersonFields
from .person_address import Address

__all__ = ("PersonUpdate",)


class PersonUpdate(BaseModel):
    """Body of Person PATCH requests"""
    name: Optional[str] = PersonFields.name
    address: Optional[Address] = PersonFields.address_update
    birth: Optional[date] = PersonFields.birth

    def model_dump(self, **kwargs) -> dict:
        # The "birth" field must be converted to string (isoformat) when exporting to dict (for Mongo)
        # TODO Better way to do this? (automatic conversion can be done with model_config['json_encoders'], but not available for dict
        d = super().model_dump(**kwargs)
        with suppress(KeyError):
            d["birth"] = d.pop("birth").isoformat()
        return d

    model_config = {"extra": "ignore"}

