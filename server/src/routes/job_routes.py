from fastapi.routing import APIRouter
from src.models.job import Job

router = APIRouter(prefix="/job")


@router.post("/", status_code=201)
async def add_job(job: Job):
    return job
