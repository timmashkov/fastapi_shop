"""
Create
Read
Update
Delete
"""
from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from .schemas import ProductCreate, ProductUpdate, ProductUpdatePartial

async def get_products(session: AsyncSession) -> list[Product]:
    """
    Асинк функция выбирает все значения таблицы Product, и возвращает их список
    :param session:
    :return: list(products)
    """
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    """
    Асинк функция выбирает значение таблицы Product по id, и возвращает его
    :param session:
    :param product_id:
    :return: Product
    """
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, data: ProductCreate) -> Product:
    """
    Асинк функция создает значение в таблице Product по id, и возвращает его
    :param session:
    :param data:
    :return: product
    """
    product = Product(**data.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product


async def update_product(session: AsyncSession,
                         product: Product,
                         data: ProductUpdate | ProductUpdatePartial,
                         partial: bool = False) -> Product:
    """
    Функция для апдейта значения в таблице
    :param session:
    :param product:
    :param data:
    :param partial:
    :return:
    """
    for name, value in data.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(session: AsyncSession, product: Product) -> None:
    """
    Функция для удаления из БД
    :param session:
    :param product:
    :return:
    """
    await session.delete(product)
    await session.commit()
