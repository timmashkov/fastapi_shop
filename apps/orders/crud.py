"""
Create
Read
Update
Delete
"""
from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import logger
from core.models import Order


async def get_orders(session: AsyncSession) -> list[Order]:
    """
    Асинк функция выбирает все значения таблицы Product, и возвращает их список
    :param session:
    :return: list(products)
    """
    try:
        stmt = select(Order).order_by(Order.id)
        result: Result = await session.execute(stmt)
        orders = result.scalars().all()
        return list(orders)
    except Exception as e:
        logger.error(f"Error {e} has been raised")


async def get_order(session: AsyncSession, order_id: int) -> Order | dict:
    """
    Асинк функция выбирает значение таблицы Product по id, и возвращает его
    :param session:
    :param order_id:
    :return: Order
    """
    try:
        stmt = select(Order).where(Order.id == order_id)
        result: Result = await session.execute(stmt)
        answer = result.scalars().one_or_none()
        if answer:
            return answer._asdict()
        return {"error": f"There is no {order_id}"}
    except Exception as e:
        logger.error(f"Error {e} has been raised")


async def create_order(session: AsyncSession, promocode: str | None = None) -> Order:
    """
    Асинк функция для создания заказа
    :param session:
    :param promocode:
    :return: Order
    """
    try:
        order = Order(promocode=promocode)
        session.add(order)
        await session.commit()
        return order
    except Exception as e:
        logger.error(f"Error {e} has been raised")


async def drop_order(order: Order, session: AsyncSession) -> dict:
    """
    Асинк функция для удаления заказа
    :param order:
    :param session:
    :return: dict
    """
    try:
        await session.delete(order)
        await session.commit()
        return {"message": f" Order {order} has been deleted"}
    except Exception as e:
        logger.error(f"Error {e} has been raised")
