from fastapi import APIRouter
from users.schemas import UserCreate
from users.crud import create

router = APIRouter(prefix="/users")


@router.post("/")
async def create_user(user: UserCreate):
    return create(user)
