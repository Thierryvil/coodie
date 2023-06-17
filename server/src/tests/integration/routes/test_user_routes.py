from controllers.token_controller import create_access_token


def test_get_user_with_valid_token(client, access_token):
    response = client.get(
        "/user",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200


def test_get_user_with_invalid_token(client):
    invalid_token = "token_invalido"
    response = client.get(
        "/user",
        headers={"Authorization": f"Bearer {invalid_token}"},
    )
    expected_error = "Token inválido ou expirado"

    assert response.status_code == 401
    assert response.json()["detail"] == expected_error


def test_get_user_with_nonexistent_user(client):
    access_token = create_access_token(999999)
    response = client.get(
        "/user",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    expected_error = "Usuário não encontrado"

    assert response.status_code == 401
    assert response.json()["detail"] == expected_error
