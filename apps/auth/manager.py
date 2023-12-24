from core.config import settings
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from apps.auth.utils import get_user_db, send_email
from core.models import User

SECRET = settings.auth_key


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """
    Main fastapi-users class with main methods
    """

    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        """
        Sending email after registration
        """
        send_email(username=user.username)
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    """
    Function for calling db for work with data
    """
    yield UserManager(user_db)
