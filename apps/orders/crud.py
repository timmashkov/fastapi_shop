"""
Create
Read
Update
Delete
"""
from sqlalchemy.engine import Result
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Order


async def get_orders(session: AsyncSession) -> list[Order]:
    """
    Асинк функция выбирает все значения таблицы Product, и возвращает их список
    :param session:
    :return: list(products)
    """
    stmt = select(Order).order_by(Order.id)
    result: Result = await session.execute(stmt)
    orders = result.scalars().all()
    return list(orders)


async def get_order(session: AsyncSession, order_id: int) -> Order | None:
    """
    Асинк функция выбирает значение таблицы Product по id, и возвращает его
    :param session:
    :param order_id:
    :return: Order
    """
    return await session.get(Order, order_id)


async def create_order(session: AsyncSession, promocode: str | None = None) -> Order:
    order = Order(promocode=promocode)
    session.add(order)
    await session.commit()
    return order


async def drop_order(session: AsyncSession, order_id: int):
    try:
        stmt = delete(Order).where(Order.id == order_id)
        await session.execute(stmt)
        await session.commit()
        return {"message": f" Order {order_id} has been deleted"}
    except Exception as e:
        return {"message": "Something went wrong", "error": e}
