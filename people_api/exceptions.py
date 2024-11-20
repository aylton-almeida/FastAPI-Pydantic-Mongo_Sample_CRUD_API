"""EXCEPTIONS
Custom exceptions that will make the API return certain HTTP responses to the client.
Each exception has a message, statuscode and response model (from models.errors).
Each exception must be raised using the kwargs (fields) of the associated model.
Exceptions can return the HTTP response model (Response/JSONResponse) and part of the response model definition.
"""

# # Native # #
from typing import Type

# # Installed # #
from fastapi.responses import JSONResponse
from fastapi import status as statuscode

# # Package # #
from .models.errors import *

__all__ = (
    "BaseAPIException", "BaseIdentifiedException",
    "NotFoundException", "AlreadyExistsException",
    "PersonNotFoundException", "PersonAlreadyExistsException",
    "get_exception_responses"
)


class BaseAPIException(Exception):
    """Base error for custom API exceptions"""
    message: str = "Generic error"
    code: int = statuscode.HTTP_500_INTERNAL_SERVER_ERROR
    model: Type[BaseError] = BaseError

    def __init__(self, **kwargs):
        kwargs.setdefault("message", self.message)
        self.message = kwargs["message"]
        self.data = self.model(**kwargs)

    def __str__(self) -> str:
        return self.message

    def response(self) -> JSONResponse:
        return JSONResponse(
            content=self.data.dict(),
            status_code=self.code
        )

    @classmethod
    def response_model(cls) -> dict:
        return {cls.code: {"model": cls.model}}


class BaseIdentifiedException(BaseAPIException):
    """Base error for exceptions related with entities, uniquely identified"""
    message: str = "Entity error"
    code: int = statuscode.HTTP_500_INTERNAL_SERVER_ERROR
    model: Type[BaseIdentifiedError] = BaseIdentifiedError

    def __init__(self, identifier: str, **kwargs):
        super().__init__(identifier=identifier, **kwargs)


class NotFoundException(BaseIdentifiedException):
    """Base error for exceptions raised because an entity does not exist"""
    message: str = "The entity does not exist"
    code: int = statuscode.HTTP_404_NOT_FOUND
    model: Type[NotFoundError] = NotFoundError


class AlreadyExistsException(BaseIdentifiedException):
    """Base error for exceptions raised because an entity already exists"""
    message: str = "The entity already exists"
    code: int = statuscode.HTTP_409_CONFLICT
    model: Type[AlreadyExistsError] = AlreadyExistsError


class PersonNotFoundException(NotFoundException):
    """Error raised when a person does not exist"""
    message: str = "The person does not exist"


class PersonAlreadyExistsException(AlreadyExistsException):
    """Error raised when a person already exists"""
    message: str = "The person already exists"


def get_exception_responses(*args: Type[BaseAPIException]) -> dict:
    """Given BaseAPIException classes, return a dict of responses used on FastAPI endpoint definition, with the format:
    {statuscode: schema, statuscode: schema, ...}"""
    responses = dict()
    for cls in args:
        responses.update(cls.response_model())
    return responses
