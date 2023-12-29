import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import vortex
from core.models.base import Base
from core.test_database import test_database
from main import app


#Base.metadata.bind = test_database.test_engine


async def override_session_dependency() -> AsyncGenerator[AsyncSession, None]:
    async with test_database.test_session_maker() as session:
        yield session


app.dependency_overrides[vortex.scoped_session_dependency] = override_session_dependency


@pytest.fixture
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def create_db():
    from alembic import context, command
    from core.config import settings

    config = context.config
    config.set_main_option("sqlalchemy.url", settings.test_config.test_url)

    command.upgrade(config, "head")
    yield
    print("Test revisions done!")
    command.downgrade(config, "base")


client = TestClient(app)


@pytest.fixture
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
