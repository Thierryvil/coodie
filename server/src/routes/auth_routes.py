from controllers.auth_controller import authenticate_user
from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from models.token import Token

router = APIRouter(prefix="/auth")


@router.post("/token", response_model=Token)
async def login(form=Depends(OAuth2PasswordRequestForm)):
    return authenticate_user(form.username, form.password)
