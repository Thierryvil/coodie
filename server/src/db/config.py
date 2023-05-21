from configs import settings
from schemas.enterprise_schema import EnterpriseSchema
from schemas.job_schema import JobSchema
from schemas.user_schema import UserSchema
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from sqlmodel import MetaData, create_engine

engine = create_engine(f"sqlite:///{settings.DATABASE_NAME}")
metadata = MetaData(bind=engine)


def create_tables():
    insp = inspect(engine)
    if not (
        insp.has_table("users")
        and insp.has_table("jobs")
        and insp.has_table("enterprises")
    ):
        metadata.create_all()


def get_session():
    session = sessionmaker(bind=engine)
    return session()
