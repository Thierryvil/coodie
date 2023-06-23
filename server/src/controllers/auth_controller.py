from controllers.token_controller import create_access_token
from controllers.user_controller import get_user_by_email
from fastapi import HTTPException, status
from utils.bcrypt import verify_password


def authenticate_user(username: str, password: str):
    user_db = get_user_by_email(username)

    if not user_db:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Credenciais inválidas",
        )

    if not verify_password(password, user_db.password):
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
