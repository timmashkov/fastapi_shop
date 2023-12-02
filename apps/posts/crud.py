from sqlalchemy import Result, delete
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Post
from .schemas import PostInput


async def create_post(session: AsyncSession, data: PostInput):
    try:
        post = Post(**data.model_dump())
        session.add(post)
        await session.commit()
        return post
    except Exception as e:
        return {"message": "something went wrong", "error": e}


async def get_post(session: AsyncSession, post_id: int):
    try:
        post = await session.get(Post, post_id)
        return post
    except Exception as e:
        return {"message": "something went wrong", "error": e}


async def del_post(post_id: int, session: AsyncSession):
    stmt = (
        delete(Post)
        .where(Post.id == post_id)
        .returning(Post.id, Post.title, Post.body, Post.user_id)
    )
    profile: Result = await session.execute(stmt)
    answer = profile.scalars().first()
    await session.commit()
    print(type(answer))
    return answer
