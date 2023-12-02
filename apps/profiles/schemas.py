from pydantic import BaseModel


class ProfileAddingSchema(BaseModel):
    first_name: str | None
    last_name: str | None
    bio: str | None


class ProfileResponseSchema(ProfileAddingSchema):
    user_id: int
