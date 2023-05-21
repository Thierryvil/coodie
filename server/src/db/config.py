from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, create_engine
from src.config import settings

# flake8: noqa
from src.schemas.enterprise_schema import EnterpriseSchema
from src.schemas.job_schema import JobSchema
from src.schemas.user_schema import UserSchema

engine = create_engine(f"sqlite:///{settings.DATABASE_NAME}")


def get_session():
    session = sessionmaker(engine)
    return session()
