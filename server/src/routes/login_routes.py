from fastapi.routing import APIRouter
from fastapi import HTTPException
from authlib.integrations.requests_client import OAuth2Session
from authlib.integrations.base_client.errors import OAuthError
from src.configs.settings import (
    AUTH0_DOMAIN, AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET
)

router = APIRouter(prefix='/login')
oauth = OAuth2Session(
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    server_metadata_url=(
        f"https://{AUTH0_DOMAIN}/.well-known/openid-configuration",
    ),
)


@router.post("/")
async def login(email: str, password: str):
    try:
        token = oauth.fetch_token(
            f"https://{AUTH0_DOMAIN}/oauth/token",
            grant_type="password",
            username=email,
            password=password,
            audience=f"https://{AUTH0_DOMAIN}/api/v2/",
        )
        if "access_token" in token:
            return {"access_token": token["access_token"]}
    except OAuthError:
        raise HTTPException(
            status_code=401, detail="Credenciais inválidas")
