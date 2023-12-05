from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import vortex
from core.models import User


async def get_user_db(
    session: AsyncSession = Depends(vortex.session_dependency),
):
    yield SQLAlchemyUserDatabase(session, User)
