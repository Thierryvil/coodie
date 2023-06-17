from os.path import abspath, dirname, join

from sqlalchemy import inspect
from sqlmodel import Session, SQLModel, create_engine

from configs import settings

# flake8: noqa
from schemas.job_schema import JobSchema
from schemas.user_schema import UserSchema, UserType
from utils.bcrypt import encrypt_password

base_dir = join(abspath(dirname(__file__)), settings.DATABASE_NAME)  # type: ignore

engine = create_engine(
    f"sqlite:///{base_dir}",
)


def create_tables():
    insp = inspect(engine)
    if not (
        insp.has_table("users")
        and insp.has_table("jobs")
        and insp.has_table("enterprises")
    ):
        SQLModel.metadata.create_all(bind=engine)


def create_puc():
    with Session(engine) as session:
        existing_user = (
            session.query(UserSchema)
            .where(UserSchema.email == settings.PUC_USER)
            .first()
        )

        if not existing_user:
            new_user = UserSchema(
                email=settings.PUC_USER,  # type: ignore
                password=encrypt_password(settings.PUC_PASSWORD),
                user_type=UserType.Enterprise,
            )

            session.add(new_user)
            session.commit()
