from fastapi.routing import APIRouter
from models.job import Job

router = APIRouter(prefix="/enterprise")


@router.post("/jobs", status_code=201)
async def add_new_job(job: Job):
    return job


@router.get("/")
async def get_all_jobs_from_an_enterprise(enterprise_id: int):
    pass
