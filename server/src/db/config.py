from sqlmodel import create_engine
from src.configs.settings import DATABASE_NAME
# flake8: noqa
from src.schemas.enterprise_schema import EnterpriseSchema
from src.schemas.job_schema import JobSchema

engine = create_engine(f"sqlite:///{DATABASE_NAME}")
