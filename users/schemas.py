from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    # username: str = Field(..., min_length=5, max_length=20)
    username: Annotated[str, MinLen(5), MaxLen(20)]
    email: EmailStr
