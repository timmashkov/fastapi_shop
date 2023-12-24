import pytest
import pytest_asyncio
from select import select
from sqlalchemy import insert

from core.models import Post, User
from core.test_database import test_database


@pytest.mark.asyncio
async def test_create_post():
    async with test_database.test_session_maker() as session:
        stmt = insert(Post).values(title="test", body="test", user_id=1)
        await session.execute(stmt)
        await session.commit()

        query = select(Post)
        result = await session.execute(query)
        assert result.all() == [("test", "test", "user_id")], "Error"
