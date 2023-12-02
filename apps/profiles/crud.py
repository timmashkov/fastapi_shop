from sqlalchemy import update, Result, delete
from sqlalchemy.ext.asyncio import AsyncSession

from apps.profiles.schemas import ProfileAddingSchema
from core.models import Profile


async def add_user_profile(session: AsyncSession,
                           user_id: int,
                           data: ProfileAddingSchema) -> Profile:
    profile = Profile(user_id=user_id,
                      first_name=data.first_name,
                      last_name=data.last_name,
                      bio=data.bio)
    session.add(profile)
    await session.commit()
    return profile


async def edit_user_profile(first_name: str,
                            session: AsyncSession,
                            data: ProfileAddingSchema):
    stmt = update(Profile)\
        .where(Profile.first_name == first_name)\
        .values(first_name=data.first_name,
                last_name=data.last_name,
                bio=data.bio).returning(Profile.id,
                                        Profile.first_name,
                                        Profile.last_name,
                                        Profile.bio,
                                        Profile.user_id)
    result: Result = await session.execute(stmt)
    answer = result.scalars().all()
    await session.commit()
    return answer


async def drop_user_profile(first_name: str, session: AsyncSession):
    stmt = delete(Profile)\
        .where(Profile.first_name == first_name)\
        .returning(Profile.id,
                   Profile.first_name,
                   Profile.last_name,
                   Profile.bio,
                   Profile.user_id)
    profile: Result = await session.execute(stmt)
    answer = profile.scalars().all()
    await session.commit()
    return answer
