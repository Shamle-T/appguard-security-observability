"""Application error definitions placeholder."""

from fastapi import Request
from fastapi.responses import JSONResponse


class AppGuardException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


async def appguard_exception_handler(request: Request, exc: AppGuardException):
    return JSONResponse(
        status_code=exc.status_code, content={"error": True, "message": exc.message}
    )
