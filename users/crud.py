from users.schemas import UserCreate


def create(user_in: UserCreate):
    user = user_in.model_dump()
    return {"success": True, "data": user}
