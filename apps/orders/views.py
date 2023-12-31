import time

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession

from apps.orders.crud import get_orders, create_order, drop_order
from apps.orders.dependecies import order_by_id
from core.database import vortex
from core.models import Order

router = APIRouter(prefix="/orders")


@router.get("/show_orders", description="Show all orders")
@cache(expire=60)
async def show_orders(
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await get_orders(session=session)


@router.get("/get_order", description="Show one orders")
async def get_order(
    order: Order = Depends(order_by_id),
):
    return order


@router.post("/add_order", description="Create new order")
async def add_order(
    promocode: str | None,
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await create_order(promocode=promocode, session=session)


@router.delete("/del_order", description="Delete order")
async def del_order(
    order: Order = Depends(order_by_id),
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await drop_order(order=order, session=session)
