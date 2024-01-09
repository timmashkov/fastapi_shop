from typing import AsyncIterator

import pytest_asyncio
from httpx import AsyncClient

from main import app


@pytest_asyncio.fixture()
async def client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client
