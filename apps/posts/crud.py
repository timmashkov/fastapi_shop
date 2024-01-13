from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import logger
from core.models import Post
from .schemas import PostInput


async def create_post(session: AsyncSession, data: PostInput) -> Post | dict:
    """
    Асинк функция для создания поста
    :param session:
    :param data:
    :return: Post
    """
    try:
        post = Post(**data.model_dump())
        session.add(post)
        await session.commit()
        return post
    except Exception as e:
        logger.error(f"Error {e} has been raised")


async def get_post(session: AsyncSession, post_id: int) -> Post | dict:
    """
    Асинк функция для получения поста
    :param session:
    :param post_id:
    :return: Post
    """
    try:
        stmt = select(Post).where(Post.id == post_id)
        result: Result = await session.execute(stmt)
        answer = result.scalars().one_or_none()
        return answer
    except Exception as e:
        logger.error(f"Error {e} has been raised")


async def del_post(post: Post, session: AsyncSession) -> dict:
    """
    Асинк функция для удаления поста
    :param post:
    :param session:
    :return: Post
    """
    try:
        await session.delete(post)
        await session.commit()
        return {"message": f"Post {post} has been deleted"}
    except Exception as e:
        logger.error(f"Error {e} has been raised")
