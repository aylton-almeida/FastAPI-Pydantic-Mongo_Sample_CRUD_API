# Based on https://docs.pydantic.dev/latest/examples/files/#json-data


from __future__ import annotations

import pathlib

from pydantic import BaseModel, EmailStr, Field, PositiveInt, model_validator


class Person(BaseModel):
    name: str
    age: PositiveInt
    email: EmailStr
    is_adult: bool = Field(False, description="Is this person an adult? (age >= 18)")

    @model_validator(mode="before")
    @classmethod
    def _set_is_adult(cls, data) -> Person:
        """Calculates if person is an adult based on age"""

        if (age := data.get("age", 0)) and age >= 18:
            data["is_adult"] = True

        return data

    model_config = {"extra": "ignore"}


json_string = pathlib.Path("person.json").read_text()
person = Person.model_validate_json(json_string)
print(repr(person))
# > Person(name='John Doe', age=30, email='john@example.com')
