from fastapi import FastAPI, Depends, HTTPException
from dotenv import find_dotenv, load_dotenv
from os import getenv
from authlib.integrations.requests_client import OAuth2Session
import logging
import sys

log = logging.getLogger('authlib')
log.addHandler(logging.StreamHandler(sys.stdout))
log.setLevel(logging.DEBUG)

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv()

AUTH0_DOMAIN = getenv("AUTH0_DOMAIN", None)
AUTH0_CLIENT_ID = getenv("AUTH0_CLIENT_ID", None)
AUTH0_CLIENT_SECRET = getenv("AUTH0_CLIENT_SECRET", None)

app = FastAPI()
auth0_session = OAuth2Session(
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    server_metadata_url=f"https://{AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def authenticate_user(email: str, password: str):
    response = auth0_session.fetch_token(
        url=f"https://{AUTH0_DOMAIN}/oauth/token",
        token_url=f"https://{AUTH0_DOMAIN}/oauth/token",
        grant_type="client_credentials",
        username=email,
        password=password,
        audience=f"https://{AUTH0_DOMAIN}/api/v2/",
        scope="read:email_provider",
    )

    if "access_token" in response:
        return response["access_token"]
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@app.post("/login")
def login(email: str, password: str):
    access_token = authenticate_user(email, password)
    return {"access_token": access_token}
