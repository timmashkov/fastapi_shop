import pytest
from sqlalchemy import insert, select

from core.models import User, Post, Profile, Product, Order
from core.test_database import test_database


class TestCreateRouters:
    """
    Класс для группировки тестов создания записей в БД по роутерам
    """
    @pytest.mark.asyncio
    async def test_create_user(self):
        async with test_database.test_session_maker() as session:
            stmt = insert(User).values(email="user@example.com",
                                       hashed_password="string",
                                       is_active=True,
                                       is_superuser=False,
                                       is_verified=False,
                                       username="string")
            await session.execute(stmt)
            await session.commit()

            query = select(User)
            result = await session.execute(query)
            assert len(result.all()) > 0

    @pytest.mark.asyncio
    async def test_create_post(self):
        async with test_database.test_session_maker() as session:
            stmt = insert(Post).values(title="string",
                                       body="string",
                                       user_id=1)
            await session.execute(stmt)
            await session.commit()

            query = select(Post)
            result = await session.execute(query)
            assert len(result.all()) > 0

    @pytest.mark.asyncio
    async def test_create_profile(self):
        async with test_database.test_session_maker() as session:
            stmt = insert(Profile).values(first_name="string",
                                          last_name="string",
                                          bio="string",
                                          user_id=1)
            await session.execute(stmt)
            await session.commit()

            query = select(Profile)
            result = await session.execute(query)
            assert len(result.all()) > 0

    @pytest.mark.asyncio
    async def test_create_products(self):
        async with test_database.test_session_maker() as session:
            stmt = insert(Product).values(name="string",
                                          description="string",
                                          price=666,
                                          user_id=1)
            await session.execute(stmt)
            await session.commit()

            query = select(Product)
            result = await session.execute(query)
            assert len(result.all()) > 0

    @pytest.mark.asyncio
    async def test_create_order(self):
        async with test_database.test_session_maker() as session:
            stmt = insert(Order).values(promocode="string")
            await session.execute(stmt)
            await session.commit()

            query = select(Order)
            result = await session.execute(query)
            assert len(result.all()) > 0
