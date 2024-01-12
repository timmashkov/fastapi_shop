import pytest
from httpx import AsyncClient
from .conftests import client


@pytest.mark.asyncio
async def test_show_users(client: AsyncClient):
    response = await client.get("apps/users/show_users")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_show_user(client: AsyncClient):
    response = await client.get("apps/users/show_user/{test}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_user(client: AsyncClient):
    response = await client.delete("apps/users/delete_user/{test}")
    assert response.status_code == 200
    assert response.json() == {"message": f"User has been deleted"}
