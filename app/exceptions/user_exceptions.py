# app/exceptions/user_exceptions.py
from .base import NotFoundException

class UserNotFoundException(NotFoundException):
    default_message = "User not found"

    def __init__(self, user_id: int | None = None, message: str | None = None):
        self.user_id = user_id
        
        if message is None and user_id is not None:
            message = f"User with ID {user_id} not found"
        
        super().__init__(message)