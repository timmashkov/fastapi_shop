import pytest
from sqlalchemy import insert, select, update, delete

from core.test_database import test_database
from core.models import User


@pytest.mark.asyncio
async def test_register():
    data = {
        "email": "pytest@test.com",
        "password": "test",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "pytest_test"
    }
    async with test_database.test_session_maker() as test_session:
        stmt = insert(User).values(username=data["username"],
                                   email=data["email"],
                                   is_active=data["is_active"],
                                   is_superuser=data["is_superuser"],
                                   is_verified=data["is_verified"],
                                   hashed_password=data["password"]
                                   )
        await test_session.execute(stmt)
        await test_session.commit()

        query = select(User)
        result = await test_session.execute(query)
        answer = result.first()
        assert len(answer) > 0


@pytest.mark.asyncio
async def test_show_users():
    async with test_database.test_session_maker() as test_session:
        query = select(User)
        result = await test_session.execute(query)
        answer = result.first()
        assert len(answer) > 0


@pytest.mark.asyncio
async def test_update_user():
    async with test_database.test_session_maker() as test_session:
        stmt = update(User
                      ).where(User.username == "pytest_test"
                              ).values(username="pytest_test_update",
                                       email="pytest_update@test.com")
        await test_session.execute(stmt)
        await test_session.commit()

        query = select(User).where(User.username == "pytest_test_update")
        result = await test_session.execute(query)
        answer = result.first()
        assert len(answer) > 0


@pytest.mark.asyncio
async def test_delete_user():
    async with test_database.test_session_maker() as test_session:
        stmt = delete(User
                      ).where(User.username == "pytest_test_update")
        await test_session.execute(stmt)
        await test_session.commit()

        query = select(User).where(User.username == "pytest_test_update")
        result = await test_session.execute(query)
        answer = result.first()
        assert not answer
