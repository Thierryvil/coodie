from db.config import engine
from schemas.user_schema import UserSchema
from sqlmodel import Session


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
