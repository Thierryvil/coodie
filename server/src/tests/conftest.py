import pytest
from app import app
from controllers.token_controller import create_access_token
from db.config import create_tables, engine
from fastapi.testclient import TestClient
from schemas.user_schema import UserSchema, UserType
from sqlmodel import Session, SQLModel


@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    create_tables()

    yield

    SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="session", autouse=True)
def client():
    return TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def access_token():
    enterprise = UserSchema(
        email="test@email.com",
        password="",
        user_type=UserType.Enterprise,
    )

    with Session(engine) as session:
        session.add(enterprise)
        session.commit()
        session.refresh(enterprise)

    return create_access_token(enterprise.id)  # type: ignore
