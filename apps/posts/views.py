from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import vortex
from core.models import Post
from .crud import create_post, get_post, del_post
from .dependencies import post_by_id
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
    post_in: Post = Depends(post_by_id),
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return post_in


@router.delete("/del_post")
async def delete_post(
    post_in: Post = Depends(post_by_id),
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await del_post(post=post_in, session=session)
