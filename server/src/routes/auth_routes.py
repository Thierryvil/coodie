from bcrypt import checkpw
from controllers.token_controller import create_access_token, decode_access_token
from controllers.user_controller import get_user_by_email, get_user_by_id
from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.token import Token

router = APIRouter(prefix="/auth")


@router.post("/token", response_model=Token)
async def login(form=Depends(OAuth2PasswordRequestForm)):
    user_db = get_user_by_email(form.username)

    if not user_db:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Credenciais inválidas")

    if not checkpw(form.password.encode("utf-8"), user_db.password.encode("utf-8")):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Credenciais inválidas")

    return {"access_token": create_access_token(user_db.id), "token_type": "bearer"}
