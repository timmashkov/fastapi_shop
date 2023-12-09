from .auth import auth_backend, fastapi_users, current_user
from .schemas import UserRead, UserCreate, UserUpdate
from fastapi import APIRouter


router = APIRouter(prefix="/auth")

router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["register"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["reset"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["verify"],
)
# роутер с эндпоинтами библиотеки
# router.include_router(
# fastapi_users.get_users_router(UserRead, UserUpdate),
# prefix="/users",
# tags=["users"],
# )
