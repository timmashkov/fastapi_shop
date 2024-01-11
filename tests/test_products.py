import pytest
from httpx import AsyncClient
from .conftests import client


@pytest.mark.asyncio
async def test_add_product(client: AsyncClient):
    response = await client.post(
        "apps/products/add_product",
        json={"name": "string", "description": "string", "price": 0},
    )
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0
