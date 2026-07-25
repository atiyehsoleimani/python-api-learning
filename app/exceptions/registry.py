from fastapi import FastAPI
from .base import AppException
from .handlers import app_exception_handler

def register_exception_handlers(app: FastAPI) -> None:
    """
    Register the generic application exception handler with FastAPI.
    
    Because FastAPI's exception handler system supports inheritance,
    registering handler for AppException automatically handles all
    subclasses (UserNotFoundException, future ProductNotFoundException, etc.).
    """
    app.add_exception_handler(AppException, app_exception_handler)