"""APP
FastAPI app definition, initialization and definition of routes
"""

# # Installed # #
import uvicorn
from fastapi import FastAPI
from fastapi import status as statuscode
from typing import List

# # Package # #
from .models import *
from .exceptions import *
from .repositories import PeopleRepository
from .middlewares import request_handler
from .settings import api_settings as settings

__all__ = ("app", "run")


app = FastAPI(
    title=settings.title
)
app.middleware("http")(request_handler)


@app.get(
    "/people",
    response_model=List[PeopleRead],
    description="List all the available persons",
    tags=["people"]
)
async def _list_people() -> List[PeopleRead]:
    # TODO Filters
    return await PeopleRepository.list()


@app.get(
    "/people/{person_id}",
    response_model=PersonRead,
    description="Get a single person by its unique ID",
    responses=get_exception_responses(PersonNotFoundException),
    tags=["people"]
)
async def _get_person(person_id: str) -> PersonRead:
    return await PeopleRepository.get(person_id)


@app.post(
    "/people",
    description="Create a new person",
    response_model=PersonRead,
    status_code=statuscode.HTTP_201_CREATED,
    responses=get_exception_responses(PersonAlreadyExistsException),
    tags=["people"]
)
async def _create_person(create: PersonCreate) -> PersonRead:
    return await PeopleRepository.create(create)


@app.patch(
    "/people/{person_id}",
    description="Update a single person by its unique ID, providing the fields to update",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(PersonNotFoundException, PersonAlreadyExistsException),
    tags=["people"]
)
async def _update_person(person_id: str, update: PersonUpdate) -> None:
    await PeopleRepository.update(person_id, update)


@app.delete(
    "/people/{person_id}",
    description="Delete a single person by its unique ID",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(PersonNotFoundException),
    tags=["people"]
)
async def _delete_person(person_id: str) -> None:
    await PeopleRepository.delete(person_id)


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level.lower()
    )

