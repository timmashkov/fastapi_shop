from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .crud import get_users, add_user, get_user, change_user, drop_user
from .schemas import UserResponseSchema, UserAddingSchema, UserUpdatePartial
from core.models import User
from core.models import db_helper
from .dependencies import user_by_id

router = APIRouter(
    prefix='/users'
)

@router.get('/', response_model=list[UserResponseSchema])
async def show_users(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await get_users(session=session)


@router.get('/{user_id}', response_model=UserResponseSchema)
async def show_user(user_id: int,
                    session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await get_user(session=session, user_id=user_id)


@router.post('/create', response_model=UserResponseSchema)
async def create_user(data: UserAddingSchema,
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await add_user(session=session, user_in=data)


@router.put('/{upd_id}')
async def update_user(user_in: UserUpdatePartial,
                      user: User = Depends(user_by_id),
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await change_user(session=session,
                             user=user,
                             data=user_in,
                             partial=True)


@router.delete('/{id}')
async def delete_user(user: User = Depends(user_by_id),
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await drop_user(session=session, user=user)
