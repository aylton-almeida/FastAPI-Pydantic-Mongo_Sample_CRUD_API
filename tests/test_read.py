"""TEST READ
Test read actions (get one, list)
"""

# # Installed # #
from fastapi import status as statuscode

# # Package # #
from .base import BaseTest
from .utils import *


class TestGet(BaseTest):
    async def test_get_existing_person(self):
        """Having an existing person, get it.
        Should return the person"""
        person = get_existing_person()

        response = await self.get_person(person.person_id)
        assert response.json() == person.model_dump()

    async def test_get_nonexisting_person(self):
        """Get a person that does not exist.
        Should return not found 404 error and the identifier"""
        person_id = get_uuid()

        response = await self.get_person(person_id, statuscode=statuscode.HTTP_404_NOT_FOUND)
        assert response.json()["identifier"] == person_id


class TestList(BaseTest):
    async def test_list_people(self):
        """Having multiple persons, list all of them.
        Should return all of them in array"""
        people = [get_existing_person() for _ in range(4)]

        response = await self.list_people()
        assert response.json() == [p.model_dump() for p in people]

