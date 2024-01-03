import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import vortex
from core.models import Base
from core.test_database import test_database
from main import app


Base.metadata.bind = test_database.test_engine


async def override_session_dependency() -> AsyncGenerator[AsyncSession, None]:
    async with test_database.test_session_maker() as session:
        yield session
        await session.close()


app.dependency_overrides[vortex.session_dependency] = override_session_dependency


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True, scope="session")
async def create_db():
    async with test_database.test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_database.test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
