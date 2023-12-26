from fastapi import status

import pytest
from sqlalchemy import insert, select

from core.models import User
from core.test_database import test_database
from tests.conftests import client


@pytest.mark.asyncio
async def test_create_user():
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
