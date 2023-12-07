from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from apps.products.crud import get_product
from core.database import vortex
from core.models import Product


async def product_by_id(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
) -> Product:
    product = await get_product(session=session, product_id=product_id)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found!",
    )
