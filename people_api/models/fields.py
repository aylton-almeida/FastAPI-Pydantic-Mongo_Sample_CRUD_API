from __future__ import annotations

from pydantic import Field, BaseModel
from typing import Optional
from ..utils import get_time, get_uuid

_string = dict(min_length=1)
_unix_ts = dict(example=get_time())

class PersonFields(BaseModel):
    name: str = Field(
        description="Full name of this person",
        example="John Smith",
        **_string
    )
    address: Optional[dict] = Field(
        description="Address object where this person live"
    )
    address_update: Optional[dict] = Field(
        description="Address object where this person live. When updating, the whole Address object is required, as it gets replaced"
    )
    birth: str = Field(
        description="Date of birth, in format YYYY-MM-DD, or Unix timestamp",
        example="1999-12-31"
    )
    age: Optional[int] = Field(
        description="Age of this person, if date of birth is specified",
        example=20
    )
    person_id: str = Field(
        description="Unique identifier of this person in the database",
        example=get_uuid(),
        min_length=36,
        max_length=36
    )
    created: Optional[int] = Field(
        alias="created",
        description="When the person was registered (Unix timestamp)",
        **_unix_ts
    )
    updated: Optional[int] = Field(
        alias="updated",
        description="When the person was updated for the last time (Unix timestamp)",
        **_unix_ts
    )


class AddressFields(BaseModel):
    street: str = Field(
        description="Main address line",
        example="22nd Bunker Hill Avenue",
        **_string
    )
    city: str = Field(
        description="City",
        example="Hamburg",
        **_string
    )
    state: str = Field(
        description="State, province and/or region",
        example="Mordor",
        **_string
    )
    zip_code: str = Field(
        description="Postal/ZIP code",
        example="19823",
        **_string
    )
