"""
Create
Read
Update
Delete
"""
from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
from .schemas import UserAddingSchema

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


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    """
    Функция для выбора юзера по id
    :param session:
    :param user_id:
    :return: User
    """
    return await session.get(User, user_id)


async def change_user(session: AsyncSession,
                      user: User,
                      data: UserAddingSchema,
                      partial: bool = False) -> User:
    """
    Функция для изменения данных юзера
    :param session:
    :param user:
    :param data:
    :param partial:
    :return:
    """
    for name, value in data.model_dump(exclude_unset=partial).items():
        setattr(User, name, value)
    await session.commit()
    return user


async def drop_user(session: AsyncSession, user: User) -> None:
    """
    Функция удаления юзера
    :param session:
    :param user:
    :return:
    """
    await session.delete(user)
    await session.commit()
