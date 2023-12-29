from typing import Annotated

from fastapi import Path, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from apps.posts.crud import get_post
from core.database import vortex
from core.models import Post


async def post_by_id(
    post_in: Annotated[int, Path],
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
) -> Post:
    post = await get_post(session=session, post_id=post_in)
    if post:
        return post
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post {post_in} not found!",
    )
