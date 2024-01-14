import asyncio

import pytest

from typing import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Base
from core.test_database import test_database
from core.database import vortex
from main import app


Base.metadata.bind = test_database.test_engine


async def override_session_dependency() -> AsyncGenerator[AsyncSession, None]:
    session = test_database.test_session_maker()
    async with session as sess:
        yield sess


app.dependency_overrides[vortex.session_dependency] = override_session_dependency


@pytest_asyncio.fixture(autouse=True, scope="session")
async def prepare_database():
    async with test_database.test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_database.test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# SETUP
@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    policy = asyncio.WindowsSelectorEventLoopPolicy()
    res = policy.new_event_loop()
    asyncio.set_event_loop(res)
    res._close = res.close
    res.close = lambda: None

    yield res

    res._close()


@pytest_asyncio.fixture(scope="session")
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
