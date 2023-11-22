"""
Create
Read
Update
Delete
"""
from sqlalchemy.engine import Result
from sqlalchemy import select, update, delete
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User, Profile
from .schemas import UserAddingSchema, ProfileAddingSchema

async def get_users(session: AsyncSession) -> list[User]:
    """
    Функция для возврата списка всех юзеров.
    :param session:
    :return:
    """
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def add_user(session: AsyncSession, user_in: UserAddingSchema) -> User:
    """
    Функция добавления юзера
    :param session:
    :param user_in:
    :return: users
    """
    users = User(**user_in.model_dump())
    session.add(users)
    await session.commit()
    return users


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


async def get_user(session: AsyncSession, username: str):
    """
    Функция для выбора юзера по id
    :param session:
    :param username:
    :return: User
    """
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()
    if user:
        return user
    else:
        return {'error': f"There is no {username}"}


async def change_user(username: str,
                      session: AsyncSession,
                      data: UserAddingSchema):
    """
    Функция для изменения данных юзера
    :param username:
    :param session:
    :param data:
    :return:
    """
    stmt = update(User)\
        .where(User.username == username)\
        .values(username=data.username)\
        .returning(User.id,
                   User.username)
    result: Result = await session.execute(stmt)
    await session.commit()
    answer = result.scalars().all()
    return answer


async def drop_user(session: AsyncSession, user: User) -> None:
    """
    Функция удаления юзера
    :param session:
    :param user:
    :return:
    """
    await session.delete(user)
    await session.commit()


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


async def get_user_with_profile(username: str, session: AsyncSession):
    """
    Функция возврата юзера и связанного с ним профиля
    вместо join попробовал joinload(гораздо удобнее)
    :param username:
    :param session:
    :return: answer
    """
    stmt = select(User).options(joinedload(User.profiles)).where(User.username == username)
    result = await session.scalars(stmt)
    answer = result.all()
    return answer
