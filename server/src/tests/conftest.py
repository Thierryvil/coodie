import pytest
from configs import settings
from db.config import create_tables, engine
from sqlmodel import SQLModel


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")


@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    create_tables()

    yield

    SQLModel.metadata.drop_all(engine)
