import pytest
from sqlalchemy import insert, select, delete

from core.test_database import test_database
from core.models import Product


@pytest.mark.asyncio
async def test_add_product():
    data = {"name": "test", "description": "test", "price": 666}
    async with test_database.test_session_maker() as test_session:
        stmt = insert(Product).values(
            name=data["name"],
            description=data["description"],
            price=data["price"],
        )
        await test_session.execute(stmt)
        await test_session.commit()

        query = select(Product)
        result = await test_session.execute(query)
        answer = result.first()
        assert len(answer) > 0


@pytest.mark.asyncio
async def test_delete_user():
    async with test_database.test_session_maker() as test_session:
        stmt = delete(Product).where(Product.id == 1)
        await test_session.execute(stmt)
        await test_session.commit()

        query = select(Product).where(Product.id == 1)
        result = await test_session.execute(query)
        answer = result.first()
        assert not answer
