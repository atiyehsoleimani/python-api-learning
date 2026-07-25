# app/exceptions/base.py

class AppException(Exception):
    """
    Base class for all application-specific exceptions.
    
    Every subclass must define:
    - status_code: The HTTP status code to return
    - default_message: The default error message if none is provided
    """
    status_code: int = 500
    default_message: str = "Internal server error"

    def __init__(self, message: str | None = None):
        self.message = message or self.default_message
        super().__init__(self.message)


class NotFoundException(AppException):
    """
    Base for all 'resource not found' errors.
    Automatically sets status_code to 404.
    """
    status_code: int = 404
    default_message: str = "Resource not found"