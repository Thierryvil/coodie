from controllers.token_controller import create_access_token
from schemas.user_schema import UserSchema, UserType


def test_job_title_not_empty(client, setup_and_teardown, access_token):
    data = {
        "title": "",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": ["clt"],
    }
    headers = {"Authorization": f"Bearer {access_token}"}

    response = client.post("/jobs", json=data, headers=headers)

    assert response.status_code == 422


def test_job_description_not_empty(client, setup_and_teardown, access_token):
    data = {
        "title": "Some Title",
        "description": "",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": ["clt"],
    }
    headers = {"Authorization": f"Bearer {access_token}"}

    response = client.post("/jobs", json=data, headers=headers)

    assert response.status_code == 422


def test_job_seniority_not_empty(client, setup_and_teardown, access_token):
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": [],
        "location": ["remoto"],
        "regime": ["clt"],
    }
    headers = {"Authorization": f"Bearer {access_token}"}

    response = client.post("/jobs", json=data, headers=headers)

    assert response.status_code == 422


def test_job_location_not_empty(client, setup_and_teardown, access_token):
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["junior"],
        "location": [],
        "regime": ["clt"],
    }
    headers = {"Authorization": f"Bearer {access_token}"}

    response = client.post("/jobs", json=data, headers=headers)

    assert response.status_code == 422


def test_job_regime_not_empty(client, setup_and_teardown, access_token):
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": [],
    }
    headers = {"Authorization": f"Bearer {access_token}"}

    response = client.post("/jobs", json=data, headers=headers)

    assert response.status_code == 422


def test_unauthorized_enterprise_and_valid_job(client, setup_and_teardown):
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": ["clt"],
    }

    response = client.post("/jobs", json=data)

    assert response.status_code == 401


def test_authorized_enterprise_and_valid_job(
    client,
    setup_and_teardown,
    access_token,
):
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": ["clt"],
    }
    headers = {"Authorization": f"Bearer {access_token}"}

    response = client.post("/jobs", json=data, headers=headers)

    assert response.status_code == 201


def test_job_valid_and_invalid_user(client, setup_and_teardown):
    candidate = UserSchema(
        email="test@email.com",
        password="any password",
        user_type=UserType.Enterprise,
    )
    token = create_access_token(candidate.id)
    data = {
        "title": "Software Developer",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": ["clt"],
    }
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/jobs", json=data, headers=headers)

    assert response.status_code == 401


def test_job_valid_and_invalid_user_type(client, setup_and_teardown):
    user = UserSchema(
        email="test@email.com",
        password="121213",
        user_type=UserType.Candidate,
    )
    access_token = create_access_token(user.id)
    data = {
        "title": "",
        "description": "Some description",
        "seniority": ["junior"],
        "location": ["remoto"],
        "regime": ["clt"],
    }
    headers = {"Authorization": f"Bearer {access_token}"}

    response = client.post("/jobs", json=data, headers=headers)

    assert response.status_code == 401


def test_get_all_jobs_from_an_enterprise(client, access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("/jobs", headers=headers)

    assert response.status_code == 200
