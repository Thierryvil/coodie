from db.config import engine
from fastapi.routing import APIRouter
from models.job import Job
from schemas.job_schema import JobSchema
from sqlmodel import Session, select

router = APIRouter(prefix="/enterprise")


@router.post("/jobs", status_code=201)
async def add_new_job(job: Job):
    return job


@router.get("/jobs")
async def get_all_jobs_from_an_enterprise(enterprise_id: int):
    with Session(engine) as session:
        query = select(JobSchema).where(JobSchema.id == enterprise_id)
        jobs = session.exec(query).all()
        jobs_data = [JobSchema.from_orm(job) for job in jobs]
        return {"jobs": jobs_data}
