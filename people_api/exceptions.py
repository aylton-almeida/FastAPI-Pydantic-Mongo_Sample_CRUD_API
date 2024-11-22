from typing import Type, Dict

from fastapi.responses import JSONResponse
from fastapi import status as statuscode
from pydantic import BaseModel, Field, model_validator

from .models.errors import *


class BaseAPIException(Exception):
    message: str = "Generic error"
    code: int = statuscode.HTTP_500_INTERNAL_SERVER_ERROR
    model: Type[BaseModel] = BaseError

    def __init__(self, **kwargs):
        kwargs.setdefault("message", self.message)
        self.message: str = kwargs["message"]
        self.data: BaseModel = self.model(**kwargs)

    def __str__(self) -> str:
        return self.message

    def response(self) -> JSONResponse:
        return JSONResponse(
            content=self.data.dict(),
            status_code=self.code
        )

    @classmethod
    def response_model(cls) -> Dict[int, Dict[str, Type[BaseModel]]]:
        return {cls.code: {"model": cls.model}}


class BaseIdentifiedException(BaseAPIException):
    message: str = "Entity error"
    code: int = statuscode.HTTP_500_INTERNAL_SERVER_ERROR
    model: Type[BaseModel] = BaseIdentifiedError

    def __init__(self, identifier: str, **kwargs):
        super().__init__(identifier=identifier, **kwargs)


class NotFoundException(BaseIdentifiedException):
    message: str = "The entity does not exist"
    code: int = statuscode.HTTP_404_NOT_FOUND
    model: Type[BaseModel] = NotFoundError


class AlreadyExistsException(BaseIdentifiedException):
    message: str = "The entity already exists"
    code: int = statuscode.HTTP_409_CONFLICT
    model: Type[BaseModel] = AlreadyExistsError


class PersonNotFoundException(NotFoundException):
    message: str = "The person does not exist"


class PersonAlreadyExistsException(AlreadyExistsException):
    message: str = "The person already exists"


def get_exception_responses(*args: Type[BaseAPIException]) -> Dict[int, Dict[str, Type[BaseModel]]]:
    responses: Dict[int, Dict[str, Type[BaseModel]]] = dict()
    for cls in args:
        responses.update(cls.response_model())
    return responses
