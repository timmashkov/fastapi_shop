from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import product_by_id
from .crud import (
    get_products,
    get_product,
    create_product,
    delete_product,
    update_product,
)
from .schemas import Product, ProductCreate, ProductUpdatePartial
from core.database import vortex

router = APIRouter(prefix="/products")


@router.get("/", response_model=list[Product])
async def take_products(
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await get_products(session=session)


@router.post("/add", response_model=Product)
async def add_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await create_product(session=session, data=product_in)


@router.get("/{id}/", response_model=Product)
async def take_product(
    id: int, session: AsyncSession = Depends(vortex.scoped_session_dependency)
):
    product = await get_product(session=session, product_id=id)
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no product with id: {id}",
    )


@router.put("/{id_upd}")
async def upd_product(
    product_upd: ProductUpdatePartial,
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
    product: Product = Depends(product_by_id),
):
    return await update_product(
        session=session, product=product, data=product_upd, partial=True
    )


@router.delete("/{id}")
async def del_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await delete_product(session=session, product=product)
