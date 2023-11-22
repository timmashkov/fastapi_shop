from pydantic import BaseModel, ConfigDict
from typing import Optional


class UserAddingSchema(BaseModel):
    """
    Базовая модель добавления юзера без id.
    """
    username: str


class ProfileAddingSchema(BaseModel):
    first_name: str | None
    last_name: str | None
    bio: str | None


class ProfileResponseSchema(ProfileAddingSchema):
    user_id: int


class UserUpdatePartial(UserAddingSchema):
    """
    Схема для частичного апдейта записи
    """
    username: str | None = None


class UserResponseSchema(UserAddingSchema):
    """
    Модель для возврата значения.
    """
    model_config = ConfigDict(from_attributes=True)
    id: int


class UserWithProfile(BaseModel):
    id: int
    username: str
    first_name: str | None
    last_name: str | None
    bio: str | None
    user_id: int
