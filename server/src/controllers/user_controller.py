from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from controllers.token_controller import decode_access_token
from db.config import engine
from schemas.user_schema import UserSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_user_by_email(email: str):
    with Session(engine) as session:
        return (
            session.query(UserSchema)
            .filter(
                UserSchema.email == email,
            )
            .first()
        )


def get_user_by_id(user_id: int):
    with Session(engine) as session:
        return (
            session.query(UserSchema)
            .filter(
                UserSchema.id == user_id,
            )
            .first()
        )


def get_current_user(token: str = Depends(oauth2_scheme)):
    user_id = decode_access_token(token)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
