from pydantic import BaseModel


class PostInput(BaseModel):
    title: str
    body: str | None
    user_id: int


class PostOutput(PostInput):
    id: int
