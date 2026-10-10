from pydantic import BaseModel, ConfigDict, Field 

class PostBase(BaseModel):
    title: str | None = None
    content: str | None = None

class PostCreate(PostBase):
    title: str = Field(min_length=1)


class PostUpdate(PostBase):
    title: str = Field(default=None, min_length=1)

class PostResponse(PostBase):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)