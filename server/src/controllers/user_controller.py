from src.db.config import get_session
from src.models.user import User
from src.schemas.user_schema import UserSchema


def get_user_by_email(email: str):
    with get_session() as session:
        return session.query(UserSchema).filter(UserSchema.email == email).first()


def get_user_by_id(user_id: int):
    with get_session() as session:
        return session.query(UserSchema).filter(UserSchema.id == user_id).first()
