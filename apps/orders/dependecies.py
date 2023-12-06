from typing import Annotated

from fastapi import Path, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from apps.orders.crud import get_order
from core.database import vortex


async def order_by_id(order_in: Annotated[int, Path],
                      session: AsyncSession = Depends(vortex.scoped_session_dependency)):
    order = await get_order(order_id=order_in, session=session)
    if order:
        return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Order {order_in} not found!",
    )
