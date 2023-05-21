import pytest
from models.job import Job


def test_job_title_not_empty():
    with pytest.raises(ValueError):
        Job(
            id=None,
            title="",
            description="Some description",
            seniority={"junior"},
            location={"remoto"},
            regime={"clt"},
        )


def test_job_description_not_empty():
    with pytest.raises(ValueError):
        Job(
            id=None,
            title="Some Title",
            description="",
            seniority={"junior"},
            location={"remoto"},
            regime={"clt"},
        )


def test_job_seniority_not_empty():
    with pytest.raises(ValueError):
        Job(
            id=None,
            title="Software Developer",
            description="Some description",
            seniority=set(),
            location={"remoto"},
            regime={"clt"},
        )


def test_job_valid_seniority():
    with pytest.raises(ValueError):
        Job(
            id=None,
            title="Software Developer",
            description="Some description",
            seniority={"estagiario"},
            location={"remoto"},
            regime={"clt"},
        )


def test_job_location_not_empty():
    with pytest.raises(ValueError):
        Job(
            id=None,
            title="Software Developer",
            description="Some description",
            seniority={"junior"},
            location=set(),
            regime={"clt"},
        )


def test_job_valid_location():
    with pytest.raises(ValueError):
        Job(
            id=None,
            title="Software Developer",
            description="Some description",
            seniority={"junior"},
            location={"office"},
            regime={"clt"},
        )


def test_job_regime_not_empty():
    with pytest.raises(ValueError):
        Job(
            id=None,
            title="Software Developer",
            description="Some description",
            seniority={"junior"},
            location={"remoto"},
            regime=set(),
        )


def test_job_valid_regime():
    with pytest.raises(ValueError):
        Job(
            id=None,
            title="Software Developer",
            description="Some description",
            seniority={"junior"},
            location={"remoto"},
            regime={"freelancer"},
        )


def test_valid_job():
    job = Job(
        id=None,
        title="Software Developer",
        description="Some description",
        seniority={"junior"},
        location={"remoto"},
        regime={"clt"},
    )
    assert job.title == "Software Developer"
    assert job.description == "Some description"
    assert job.seniority == {"junior"}
    assert job.location == {"remoto"}
    assert job.regime == {"clt"}
