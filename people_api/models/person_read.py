"""MODELS - PERSON - READ
Person Read model. Inherits from PersonCreate and adds the person_id field, which is the _id field on Mongo documents
"""

# # Native # #
from datetime import datetime
from typing import List

from dateutil.relativedelta import relativedelta

# # Installed # #
from pydantic import model_validator

from .fields import PersonFields

# # Package # #
from .person_create import PersonCreate

__all__ = ("PersonRead", "PeopleRead")


class PersonRead(PersonCreate):
    """Body of Person GET and POST responses"""

    person_id: str = PersonFields.person_id
    age: int | None = PersonFields.age
    created: int = PersonFields.created
    updated: int = PersonFields.updated

    @model_validator(mode="before")
    @classmethod
    def _set_person_id(cls, data):
        """Swap the field _id to person_id (this could be done with field alias, by setting the field as "_id"
        and the alias as "person_id", but can be quite confusing)"""
        document_id = data.get("_id")
        if document_id:
            data["person_id"] = document_id
        return data

    @model_validator(mode="before")
    @classmethod
    def _set_age(cls, data):
        """Calculate the current age of the person from the date of birth, if any"""

        if birth_str := data.get("birth"):
            birth = datetime.fromisoformat(birth_str)
            if birth:
                today = datetime.now().date()
                data["age"] = relativedelta(today, birth).years

        return data

    model_config = {
        "extra": "ignore"
    }  # if a read document has extra fields, ignore them


PeopleRead = List[PersonRead]
