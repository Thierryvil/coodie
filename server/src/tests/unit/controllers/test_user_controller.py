from controllers.user_controller import get_user_by_email
from db.config import engine
from schemas.user_schema import UserSchema, UserType
from sqlmodel import Session


def test_invalid_user_get_email(setup_and_teardown):
    assert get_user_by_email("invalid@email.com") is None


def test_valid_user_get_email(setup_and_teardown):
    with Session(engine) as session:
        user = UserSchema(
            email="valid@email.com",
            password="any password",
            user_type=UserType.Candidate,
        )
        session.add(user)
        session.commit()
        session.refresh(user)

    assert get_user_by_email("valid@email.com") == user
