from fastapi import HTTPException, status
from sqlmodel import Session, select

from db.config import engine
from schemas.job_schema import JobSchema
from schemas.user_schema import UserType


def create_new_job(job, user):
    if not user.user_type == UserType.Enterprise:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)
    with Session(engine) as session:
        job_schema = JobSchema(**job.dict())
        job_schema.location = ",".join(job.location)
        job_schema.seniority = ",".join(job.seniority)
        job_schema.regime = ",".join(job.regime)
        job_schema.enterprise_id = user.id
        session.add(job_schema)
        session.commit()
        session.refresh(job_schema)
        return job_schema


def get_all_jobs(user):
    with Session(engine) as session:
        query = select(JobSchema).where(JobSchema.enterprise_id == user.id)
        jobs = session.exec(query).all()
        jobs_data = [JobSchema.from_orm(job) for job in jobs]
        return jobs_data
