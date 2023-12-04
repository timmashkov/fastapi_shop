import secrets
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from starlette import status

router = APIRouter(
    prefix="/auth"
)

security = HTTPBasic()


@router.get("/auth")
async def get_auth(credential: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {'message': 'hello', 'data': credential}


data = {'admin': 'admin', 'user': 'password'}


async def take_username(credential: Annotated[HTTPBasicCredentials, Depends(security)]):
    unauth = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid data")
    correct_password = data.get(credential.username)
    if correct_password is None:
        raise unauth
    if credential.username not in data:
        raise unauth
    if not secrets.compare_digest(credential.password.encode("utf-8"), correct_password.encode("utf-8")):
        raise unauth
    return credential.username


@router.get("/auth")
async def get_auth_user(auth_username: str = Depends(take_username)):
    return {'message': 'hello', 'data': auth_username}
