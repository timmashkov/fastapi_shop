from sqlalchemy import update, Result, delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.profiles.schemas import ProfileAddingSchema
from core.models import Profile, User


async def add_user_profile(
    session: AsyncSession, user_id: int, data: ProfileAddingSchema
) -> Profile:
    profile = Profile(
        user_id=user_id,
        first_name=data.first_name,
        last_name=data.last_name,
        bio=data.bio,
    )
    session.add(profile)
    await session.commit()
    return profile


async def edit_user_profile(
    first_name: str, session: AsyncSession, data: ProfileAddingSchema
):
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
    answer = result.scalars().all()
    await session.commit()
    return answer


async def drop_user_profile(session: AsyncSession, profile: Profile):
    try:
        await session.delete(profile)
        await session.commit()
        return {"message": f"Profile {profile} has been deleted"}
    except Exception as e:
        return {"message": "something went wrong", "error": e}


async def get_profile(session: AsyncSession, profile_id: int):
    stmt = select(Profile).where(Profile.id == profile_id)
    result: Result = await session.execute(stmt)
    answer = result.scalars().one_or_none()
    if answer:
        return answer
    return {"error": f"There is no {profile_id}"}
