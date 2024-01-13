from sqlalchemy import update, Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.profiles.schemas import ProfileAddingSchema
from core.config import logger
from core.models import Profile


async def add_user_profile(
    session: AsyncSession, user_id: int, data: ProfileAddingSchema
) -> Profile:
    """
    Асинк функция для создания профиля
    :param session:
    :param user_id:
    :param data:
    :return: Profile
    """
    try:
        profile = Profile(
            user_id=user_id,
            first_name=data.first_name,
            last_name=data.last_name,
            bio=data.bio,
        )
        session.add(profile)
        await session.commit()
        return profile
    except Exception as e:
        logger.error(f"Error {e} has been raised")


async def edit_user_profile(
    first_name: str, session: AsyncSession, data: ProfileAddingSchema
) -> dict:
    """
    Асинк функция для изменения профиля
    :param first_name:
    :param session:
    :param data:
    :return:
    """
    try:
        stmt = (
            update(Profile)
            .where(Profile.first_name == first_name)
            .values(first_name=data.first_name, last_name=data.last_name, bio=data.bio)
            .returning(
                Profile.id,
                Profile.first_name,
                Profile.last_name,
                Profile.bio,
                Profile.user_id,
            )
        )
        result: Result = await session.execute(stmt)
        answer = result.first()
        await session.commit()
        return answer._asdict()
    except Exception as e:
        logger.error(f"Error {e} has been raised")


async def drop_user_profile(session: AsyncSession, profile: Profile) -> dict:
    """
    Асинк функция для удаления профиля
    :param session:
    :param profile:
    :return:
    """
    try:
        await session.delete(profile)
        await session.commit()
        return {"message": f"Profile {profile} has been deleted"}
    except Exception as e:
        logger.error(f"Error {e} has been raised")


async def get_profile(session: AsyncSession, profile_id: int) -> Profile | dict:
    """
    Асинк функция для получения профиля
    :param session:
    :param profile_id:
    :return:
    """
    try:
        stmt = select(Profile).where(Profile.id == profile_id)
        result: Result = await session.execute(stmt)
        answer = result.scalars().one_or_none()
        if answer:
            return answer._asdict()
        return {"error": f"There is no {profile_id}"}
    except Exception as e:
        logger.error(f"Error {e} has been raised")
