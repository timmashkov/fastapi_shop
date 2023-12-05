import secrets
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from starlette import status

router = APIRouter(
    prefix="/auth"
)

security = HTTPBasic()


