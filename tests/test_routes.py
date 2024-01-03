import pytest
from httpx import AsyncClient
from .conftests import ac


@pytest.mark.parametrize(
    "request_body",
    [
        (
            {
                "email": "test@example.com",
                "password": "test",
                "is_active": "true",
                "is_superuser": "false",
                "is_verified": "false",
                "username": "test",
            }
        )
    ],
)
async def test_create_user(ac: AsyncClient, request_body):
    response = await ac.post("apps/auth/auth/register", json=request_body)

    assert response.status_code == 201


@pytest.mark.parametrize(
    "request_body",
    [
        (
            {
                'title': "test",
                "body": "test",
                "user_id": 6
            }
        )
    ],
                         )
async def test_create_post(ac: AsyncClient, request_body):
    response = await ac.put("apps/post/add_post", json=request_body)

    assert response.status_code == 200
