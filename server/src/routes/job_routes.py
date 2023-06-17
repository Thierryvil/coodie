from typing import Annotated

from fastapi import Depends
from fastapi.routing import APIRouter

from controllers.job_controller import create_new_job, get_all_jobs
from models.job import Job
from routes.user_router import get_current_user
from schemas.user_schema import UserSchema

router = APIRouter(prefix="/jobs")


@router.post("/", status_code=201)
async def add_new_job(
    user: Annotated[UserSchema, Depends(get_current_user)],
    job: Job,
):
    return create_new_job(job, user)


@router.get("/")
async def get_all_jobs_from_enterprise(
    user: Annotated[UserSchema, Depends(get_current_user)]
):
    return get_all_jobs(user)
