import pytest
from fastapi import Depends
from sqlalchemy import insert, select, Result

from sqlalchemy.ext.asyncio import AsyncSession

from core.test_database import test_database
from core.models import Post, User


async def test_get_user():
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

    async with test_database.test_session_maker() as test_session:
        query = select(User)
        result = await test_session.execute(query)
        answer = result.first()
        assert len(answer) > 0
