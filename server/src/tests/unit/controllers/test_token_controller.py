from controllers.token_controller import decode_access_token


def test_decoded_invalid_token():
    assert decode_access_token("invalid") is None
