import logging

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from controllers.token_controller import create_access_token
from controllers.user_controller import get_user_by_email
from models.token import Token
from utils.bcrypt import verify_password

router = APIRouter(prefix="/auth")


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


@router.post("/token", response_model=Token)
async def login(form=Depends(OAuth2PasswordRequestForm)):
    user_db = get_user_by_email(form.username)
    logging.info(
        f"COODIE LOG == USERNAME: '{form.username}' PASSWORD: '{form.password} "
        f"ON DB: '{user_db}'"
    )

    if not user_db:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Credenciais inválidas",
        )

    if not verify_password(form.password, user_db.password):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Credenciais inválidas",
        )

    return {
        "user": {
            "id": user_db.id,
            "username": user_db.email,
        },
        "access_token": create_access_token(user_db.id),
        "token_type": "bearer",
    }
