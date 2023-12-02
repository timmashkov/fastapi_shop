from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User

from . import crud


async def user_by_id(
    user_in: Annotated[str, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:
    product = await crud.get_user(session=session, username=user_in)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {user_in} not found!",
    )
