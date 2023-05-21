from configs import settings

# flake8: noqa
from schemas.enterprise_schema import EnterpriseSchema
from schemas.job_schema import JobSchema
from schemas.user_schema import UserSchema
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine

engine = create_engine(f"sqlite:///{settings.DATABASE_NAME}")


def create_tables():
    insp = inspect(engine)
    if not (
        insp.has_table("users")
        and insp.has_table("jobs")
        and insp.has_table("enterprises")
    ):
        SQLModel.metadata.create_all(bind=engine)


def get_session():
    session = sessionmaker(bind=engine)
    return session()
