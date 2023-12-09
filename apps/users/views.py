from fastapi import APIRouter, Depends, Request, BackgroundTasks
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse
from .crud import (
    get_users,
    add_user,
    get_user,
    change_user,
    drop_user,
    get_user_with_profile,
    get_user_with_post,
    get_user_with_products,
    get_user_with_profile_and_products,
)
from .schemas import UserResponseSchema, UserAddingSchema, UserUpdatePartial
from core.models import User
from core.database import vortex
from .dependencies import user_by_id
from ..auth import current_user

router = APIRouter(prefix="/users")


@router.get("/", response_model=list[UserResponseSchema])
@cache(expire=60)
async def show_users(session: AsyncSession = Depends(vortex.scoped_session_dependency)):
    return await get_users(session=session)


@router.get("/{username}")
@cache(expire=60)
async def show_user(
    username: str, session: AsyncSession = Depends(vortex.scoped_session_dependency)
):
    return await get_user(session=session, username=username)


@router.get("/user_profile/{username}")
@cache(expire=60)
async def get_all(
    username: str, session: AsyncSession = Depends(vortex.scoped_session_dependency)
):
    return await get_user_with_profile(username=username, session=session)


@router.get("/user_post/")
@cache(expire=60)
async def get_users_posts(
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await get_user_with_post(session=session)


@router.get("/user_product/")
@cache(expire=60)
async def get_users_product(
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await get_user_with_products(session=session)


@router.get("/user_product_profile/")
@cache(expire=60)
async def get_users_product_profile(
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await get_user_with_profile_and_products(session=session)


@router.post("/create", response_model=UserResponseSchema)
async def create_user(
    data: UserAddingSchema,
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await add_user(session=session, user_in=data)


@router.put("/{username}", response_model=UserUpdatePartial)
async def update_user(
    username: str,
    user_in: UserUpdatePartial,
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await change_user(session=session, username=username, data=user_in)


@router.delete("/{id}")
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await drop_user(session=session, user=user)
