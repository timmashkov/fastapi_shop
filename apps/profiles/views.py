from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.profiles.crud import add_user_profile, edit_user_profile, drop_user_profile
from apps.profiles.schemas import ProfileResponseSchema, ProfileAddingSchema
from core.database import vortex

router = APIRouter(prefix="/profile")


@router.post("/create_profile/{user_id}", response_model=ProfileResponseSchema)
async def create_profile(
    user_id: int,
    data: ProfileAddingSchema,
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await add_user_profile(session=session, user_id=user_id, data=data)


@router.put("/profile/{first_name}")
async def update_profile(
    first_name: str,
    profile_in: ProfileAddingSchema,
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
):
    return await edit_user_profile(
        first_name=first_name, data=profile_in, session=session
    )


@router.delete("/profile/{first_name}")
async def delete_profile(
    first_name: str, session: AsyncSession = Depends(vortex.scoped_session_dependency)
):
    return await drop_user_profile(first_name=first_name, session=session)
