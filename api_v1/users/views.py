from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .crud import get_users, add_user, get_user, change_user, drop_user, add_user_profile, \
    edit_user_profile, drop_user_profile, get_user_with_profile
from .schemas import UserResponseSchema, UserAddingSchema, UserUpdatePartial, \
    ProfileResponseSchema, ProfileAddingSchema, UserWithProfile
from core.models import User
from core.models import db_helper
from .dependencies import user_by_id

router = APIRouter(
    prefix='/users'
)

@router.get('/', response_model=list[UserResponseSchema])
async def show_users(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await get_users(session=session)


@router.get('/{username}')
async def show_user(username: str,
                    session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await get_user(session=session, username=username)


@router.get('/mixed/{username}')
async def get_all(username: str,
                  session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await get_user_with_profile(username=username, session=session)


@router.post('/create', response_model=UserResponseSchema)
async def create_user(data: UserAddingSchema,
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await add_user(session=session, user_in=data)


@router.post('/create_profile/{user_id}', response_model=ProfileResponseSchema)
async def create_profile(user_id: int,
                         data: ProfileAddingSchema,
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await add_user_profile(session=session, user_id=user_id, data=data)


@router.put('/{username}')
async def update_user(username: str,
                      user_in: UserUpdatePartial,
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await change_user(session=session,
                             username=username,
                             data=user_in)


@router.put('/profile/{first_name}')
async def update_profile(first_name: str,
                         profile_in: ProfileAddingSchema,
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await edit_user_profile(first_name=first_name, data=profile_in, session=session)


@router.delete('/{id}')
async def delete_user(user: User = Depends(user_by_id),
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await drop_user(session=session, user=user)


@router.delete('/profile/{first_name}')
async def delete_profile(first_name: str,
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await drop_user_profile(first_name=first_name, session=session)
