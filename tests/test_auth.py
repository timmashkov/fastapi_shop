from tests.conftests import client


async def test_register():
    client.post(
        "auth/register",
        json={
            "email": "user1@example.com",
            "password": "string",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "username": "string",
        },
    )


