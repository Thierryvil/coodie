from os import getenv
from dotenv import load_dotenv

load_dotenv()
AUTH0_DOMAIN = getenv("AUTH0_DOMAIN", None)
AUTH0_CLIENT_ID = getenv("AUTH0_CLIENT_ID", None)
AUTH0_CLIENT_SECRET = getenv("AUTH0_CLIENT_SECRET", None)
DATABASE_NAME = getenv("DATABASE_NAME", 'test.db')
