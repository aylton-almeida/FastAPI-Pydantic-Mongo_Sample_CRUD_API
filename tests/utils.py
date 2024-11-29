"""TEST - UTILS
Misc helpers/utils functions for tests
"""

# # Native # #
from datetime import datetime
from random import randint

# # Project # #
from people_api.models import *
from people_api.repositories import PeopleRepository
from people_api.utils import get_uuid

__all__ = ("get_person_create", "get_existing_person", "get_uuid")


def get_address(**kwargs) -> Address:
    return Address.model_validate(
        {
            "street": get_uuid(),
            "city": get_uuid(),
            "state": get_uuid(),
            "zip_code": randint(1000, 10000),
            **kwargs,
        }
    )


def get_person_create(**kwargs) -> PersonCreate:
    return PersonCreate.model_validate(
        {
            "name": get_uuid(),
            "address": get_address(),
            "birth": datetime.now().date(),
            **kwargs,
        }
    )


async def get_existing_person(**kwargs) -> Person:
    return await PeopleRepository.create(get_person_create(**kwargs))

