from typing import Annotated

from controllers.user_controller import get_current_user
from fastapi import APIRouter, Depends
from schemas.user_schema import UserSchema

router = APIRouter(prefix="/user")


@router.get("/")
async def get_user(user: Annotated[UserSchema, Depends(get_current_user)]):
    return user
