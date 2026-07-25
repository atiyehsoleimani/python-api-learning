# app/exceptions/handlers.py
from fastapi import Request
from fastapi.responses import JSONResponse
from .base import AppException

async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    """
    Generic handler for all application exceptions.
    
    Relies on polymorphism: each exception subclass defines its own
    status_code and message via class attributes.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )