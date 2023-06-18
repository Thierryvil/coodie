import pytest
from fastapi import HTTPException

from controllers.job_controller import create_new_job
from models.job import Job
from schemas.user_schema import UserSchema, UserType


def test_create_new_job(setup_and_teardown):
    user = UserSchema(
        email="test@email.com",
        password="123456",
        user_type=UserType.Enterprise,
    )
    job = Job(
        title="Backend Developer",
        description="Develop backend",
        location=["remoto"],
        seniority=["junior"],
        regime=["clt"],
    )

    new_job = create_new_job(job, user)
    assert new_job.title == job.title
    assert new_job.description == job.description
    assert new_job.location == "remoto"
    assert new_job.seniority == "junior"
    assert new_job.regime == "clt"
    assert new_job.enterprise_id == user.id


def test_create_new_job_with_invalid_user_type(setup_and_teardown):
    user = UserSchema(
        email="test@email.com",
        password="123456",
        user_type=UserType.Candidate,
    )
    job = Job(
        title="Backend Developer",
        description="Develop backend",
        location=["remoto"],
        seniority=["junior"],
        regime=["clt"],
    )

    with pytest.raises(HTTPException):
        create_new_job(job, user)