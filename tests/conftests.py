import asyncio
from typing import AsyncGenerator

import pytest_asyncio
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import vortex
from core.models.base import Base
from core.test_database import test_database
from main import app


Base.metadata.bind = test_database


async def override_session_dependency() -> AsyncGenerator[AsyncSession, None]:
    async with test_database.test_session_maker() as session:
        yield session

app.dependency_overrides[vortex.session_dependency] = override_session_dependency


@pytest_asyncio.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest_asyncio.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
