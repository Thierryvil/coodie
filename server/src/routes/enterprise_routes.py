from db.config import engine
from fastapi import HTTPException, status
from fastapi.routing import APIRouter
from models.job import Job
from schemas.job_schema import JobSchema
from sqlmodel import Session, select

router = APIRouter(prefix="/enterprise")


@router.post("/jobs", status_code=201)
async def add_new_job(job: Job):
    with Session(engine) as session:
        try:
            job_schema = JobSchema(**job.dict())
            job_schema.location = ",".join(job.location)
            job_schema.seniority = ",".join(job.seniority)
            job_schema.regime = ",".join(job.regime)
            session.add(job_schema)
            session.commit()
            session.refresh(job_schema)
            return job_schema
        except Exception as e:
            session.rollback()
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ocorreu algum erro ao inserir uma nova vaga",
            ) from e
        finally:
            session.close()


@router.get("/jobs")
async def get_all_jobs_from_an_enterprise(enterprise_id: int):
    with Session(engine) as session:
        query = select(JobSchema).where(JobSchema.id == enterprise_id)
        jobs = session.exec(query).all()
        jobs_data = [JobSchema.from_orm(job) for job in jobs]
        return {"jobs": jobs_data}
