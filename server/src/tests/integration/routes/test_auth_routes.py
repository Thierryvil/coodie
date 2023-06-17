from db.config import engine
from fastapi.testclient import TestClient
from schemas.user_schema import UserSchema, UserType
from sqlmodel import Session
from utils.bcrypt import encrypt_password


def test_auth_with_invalid_user_and_valid_password(
    client: TestClient,
    setup_and_teardown,
):
    with Session(engine) as session:
        user = UserSchema(
            email="test@email.com",
            password=encrypt_password("valid password"),
            user_type=UserType.Enterprise,
        )
        session.add(user)
        session.commit()
        session.refresh(user)

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"username": "invalid@email.com", "password": "valid password"}

    response = client.post("/auth/token", headers=headers, data=data)

    assert response.status_code == 401


def test_auth_with_valid_user_and_invalid_password(
    client: TestClient,
    setup_and_teardown,
):
    with Session(engine) as session:
        user = UserSchema(
            email="email@email.com",
            password=encrypt_password("password"),
            user_type=UserType.Enterprise,
        )
        session.add(user)
        session.commit()
        session.refresh(user)

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"username": "email@email.com", "password": "any password"}

    response = client.post("/auth/token", headers=headers, data=data)

    assert response.status_code == 401


def test_auth_valid_user_and_alid_password(
    client: TestClient,
    setup_and_teardown,
):
    with Session(engine) as session:
        user = UserSchema(
            email="email@email.com",
            password=encrypt_password("password"),
            user_type=UserType.Enterprise,
        )
        session.add(user)
        session.commit()
        session.refresh(user)

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"username": "email@email.com", "password": "password"}

    response = client.post("/auth/token", headers=headers, data=data)

    assert response.status_code == 200
    assert "access_token" in response.json()
