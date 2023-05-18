from fastapi import FastAPI, Depends, HTTPException
from dotenv import find_dotenv, load_dotenv
from os import getenv
from authlib.integrations.requests_client import OAuth2Session
from authlib.integrations.base_client.errors import OAuthError
import logging
from fastapi.middleware.cors import CORSMiddleware

log = logging.getLogger('authlib')
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv()

AUTH0_DOMAIN = getenv("AUTH0_DOMAIN", None)
AUTH0_CLIENT_ID = getenv("AUTH0_CLIENT_ID", None)
AUTH0_CLIENT_SECRET = getenv("AUTH0_CLIENT_SECRET", None)

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


oauth = OAuth2Session(
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    server_metadata_url=f'https://{AUTH0_DOMAIN}/.well-known/openid-configuration',
)


@app.post("/login")
def login(email: str, password: str):
    try:
        token = oauth.fetch_token(
            f"https://{AUTH0_DOMAIN}/oauth/token",
            grant_type="password",
            username=email,
            password=password,
            audience=f'https://{AUTH0_DOMAIN}/api/v2/'
        )
        if "access_token" in token:
            return {"access_token": token["access_token"]}
    except OAuthError:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
        