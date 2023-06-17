from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


class Token(BaseModel):
    user: User
    access_token: str
    token_type: str
