from datetime import datetime, timedelta

from configs import settings
from jose import JWTError, jwt


def create_access_token(user_id: int) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES  # type: ignore
    )
    to_encode = {"user_id": user_id, "exp": expire}
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,  # type: ignore
        algorithm=settings.ALGORITHM,  # type: ignore
    )
    return encoded_jwt


def decode_access_token(token: str):
    try:
        decoded_token = jwt.decode(
            token,
            settings.SECRET_KEY,  # type: ignore
            algorithms=[
                settings.ALGORITHM,  # type: ignore
            ],
        )
        user_id = decoded_token.get("user_id")
        return user_id
    except JWTError:
        return None
