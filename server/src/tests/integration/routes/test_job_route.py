from app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_job_title_not_empty():
    data = {
        "title": "",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": ["clt"],
    }

    response = client.post("/enterprise/jobs", json=data)
    assert response.status_code == 422


def test_job_description_not_empty():
    data = {
        "title": "Some Title",
        "description": "",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": ["clt"],
    }
    response = client.post("/enterprise/jobs", json=data)
    assert response.status_code == 422


def test_job_seniority_not_empty():
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": [],
        "location": ["remoto"],
        "regime": ["clt"],
    }
    response = client.post("/enterprise/jobs", json=data)
    assert response.status_code == 422


def test_job_valid_seniority():
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["estagiario"],
        "location": ["remoto"],
        "regime": ["clt"],
    }
    response = client.post("/enterprise/jobs", json=data)
    assert response.status_code == 422


def test_job_location_not_empty():
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["junior"],
        "location": [],
        "regime": ["clt"],
    }
    response = client.post("/enterprise/jobs", json=data)
    assert response.status_code == 422


def test_job_valid_location():
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["office"],
        "regime": ["clt"],
    }
    response = client.post("/enterprise/jobs", json=data)
    assert response.status_code == 422


def test_job_regime_not_empty():
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": [],
    }
    response = client.post("/enterprise/jobs", json=data)
    assert response.status_code == 422


def test_job_valid_regime():
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": ["freelancer"],
    }
    response = client.post("/enterprise/jobs", json=data)
    assert response.status_code == 422


def test_valid_job():
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": ["clt"],
    }
    response = client.post("/enterprise/jobs", json=data)
    assert response.status_code == 201
    assert response.json() == {
        "id": None,
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": ["clt"],
    }
