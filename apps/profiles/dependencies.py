from typing import Annotated

from fastapi import Path, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from apps.profiles.crud import get_profile
from core.database import vortex


async def profile_by_id(
    profile_in: Annotated[int, Path],
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    profile = await get_profile(session=session, profile_id=profile_in)
    if profile:
        return profile
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {profile_in} not found!",
    )
