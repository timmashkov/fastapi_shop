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


async def get_user(session: AsyncSession, username: str) -> User | dict:
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
        return {"error": f"There is no {username}"}


async def change_user(
    username: str, session: AsyncSession, data: UserAddingSchema
) -> dict:
    """
    Функция для изменения данных юзера
    :param username:
    :param session:
    :param data:
    :return:
    """
    stmt = (
        update(User)
        .where(User.username == username,
               )
        .values(username=data.username,
                email=data.email)
        .returning(User.id, User.username, User.email)
    )
    result: Result = await session.execute(stmt)
    await session.commit()
    answer = result.first()
    return answer._asdict()


async def drop_user(session: AsyncSession, user: str) -> dict:
    """
    Функция удаления юзера
    :param session:
    :param user:
    :return:
    """
    try:
        stmt = delete(User).where(User.username == user)
        await session.execute(stmt)
        await session.commit()
        return {"message": f"User has been deleted"}
    except Exception as e:
        return {"message": "something went wrong", "error": e}


async def get_user_with_profile(username: str, session: AsyncSession) -> dict | None:
    """
    Функция возврата юзера и связанного с ним профиля
    вместо join попробовал joinload(гораздо удобнее)
    :param username:
    :param session:
    :return: answer
    """
    try:
        stmt = (
            select(User)
            .options(joinedload(User.profiles))
            .where(User.username == username)
        )
        result = await session.scalars(stmt)
        answer = result.all()
        return answer
    except Exception as e:
        return {"message": "something went wrong", "error": e}


async def get_user_with_post(session: AsyncSession):
    stmt = select(User).options(joinedload(User.post_link)).order_by(User.id)
    users = await session.execute(stmt)
    answer = users.unique().scalars().all()
    return answer
