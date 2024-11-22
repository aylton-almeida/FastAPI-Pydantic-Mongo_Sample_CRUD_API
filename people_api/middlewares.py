from __future__ import annotations

from fastapi import Request
from typing import Callable, Any
from .exceptions import BaseAPIException

__all__ = ("request_handler",)


async def request_handler(request: Request, call_next: Callable[[Request], Any]):
    """Middleware used to process each request on FastAPI, to provide error handling (convert exceptions to responses).
    TODO: add logging and individual request traceability
    """
    try:
        return await call_next(request)

    except Exception as ex:
        if isinstance(ex, BaseAPIException):
            return ex.response()

        # Re-raising other exceptions will return internal error 500 to the client
        raise ex
