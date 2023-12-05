from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.orders.crud import get_orders, create_order, drop_order
from core.database import vortex

router = APIRouter(prefix="/orders")


@router.get("/show_orders")
async def show_orders(
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await get_orders(session=session)


@router.post("/add_order")
async def add_order(
    promocode: str | None,
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await create_order(promocode=promocode, session=session)


@router.delete("/del_order")
async def del_order(
    order_id: int, session: AsyncSession = Depends(vortex.scoped_session_dependency)
):
    return await drop_order(order_id=order_id, session=session)
