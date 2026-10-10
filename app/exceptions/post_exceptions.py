from .base import NotFoundException

class PostNotFoundException(NotFoundException):
    default_message = "Post not found"

    def __init__(self, post_id: int | None = None, message: str | None = None):
        self.post_id = post_id
        
        if message is None and post_id is not None:
            message = f"Post with ID {post_id} not found"
        
        super().__init__(message)