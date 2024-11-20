"""MODELS - FIELDS
Definition of Fields used on model classes attributes.
We define them separately because the PersonUpdate and PersonCreate models need to re-define their attributes,
as they change from Optional to required.
Address could define its fields on the model itself, but we define them here for convenience
"""

# # Installed # #
from pydantic import Field

# # Package # #
from ..utils import get_time, get_uuid

__all__ = ("PersonFields", "AddressFields")

_string = dict(min_length=1)
"""Common attributes for all String fields"""
_unix_ts = dict(example=get_time())
"""Common attributes for all Unix timestamp fields"""


class PersonFields:
    name: str = Field(
        description="Full name of this person",
        example="John Smith",
        **_string
    )
    address: str = Field(
        description="Address object where this person live"
    )
    address_update: str = Field(
        description=f"{address.description}. When updating, the whole Address object is required, as it gets replaced"
    )
    birth: str = Field(
        description="Date of birth, in format YYYY-MM-DD, or Unix timestamp",
        example="1999-12-31"
    )
    age: int = Field(
        description="Age of this person, if date of birth is specified",
        example=20
    )
    person_id: str = Field(
        description="Unique identifier of this person in the database",
        example=get_uuid(),
        min_length=36,
        max_length=36
    )
    """The person_id is the _id field of Mongo documents, and is set on PeopleRepository.create"""

    created: int = Field(
        alias="created",
        description="When the person was registered (Unix timestamp)",
        **_unix_ts
    )
    """Created is set on PeopleRepository.create"""
    updated: int = Field(
        alias="updated",
        description="When the person was updated for the last time (Unix timestamp)",
        **_unix_ts
    )
    """Created is set on PeopleRepository.update (and initially on create)"""


class AddressFields:
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

