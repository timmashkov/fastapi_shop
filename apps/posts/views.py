from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import vortex
from .crud import create_post, get_post, del_post
from .schemas import PostOutput, PostInput


router = APIRouter(prefix="/post")


@router.put("/add_post", response_model=PostOutput)
async def add_post(
    post_in: PostInput,
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await create_post(session=session, data=post_in)


@router.get("/get_post")
async def take_post(
    post_id: int, session: AsyncSession = Depends(vortex.scoped_session_dependency)
):
    return await get_post(post_id=post_id, session=session)


@router.delete("/del_post")
async def delete_post(
    post_id: int, session: AsyncSession = Depends(vortex.scoped_session_dependency)
):
    return await del_post(post_id=post_id, session=session)
