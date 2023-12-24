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

# DATABASE

Base.metadata.bind = test_database.test_engine


async def override_scoped_session_dependency() -> AsyncGenerator[AsyncSession, None]:
    async with test_database.test_session_maker() as session:
        yield session

app.dependency_overrides[vortex.scoped_session_dependency] = override_scoped_session_dependency


@pytest_asyncio.fixture(scope="session")
def event_loop(request):
    """Creating event loop for tests"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest_asyncio.fixture(scope="session")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
