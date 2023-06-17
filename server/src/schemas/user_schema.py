from enum import Enum

from sqlmodel import Field, SQLModel


class UserType(str, Enum):
    Enterprise = "empresa"
    Candidate = "candidato"
    Administrador = "administrador"


class UserSchema(SQLModel, table=True):
    __tablename__: str = "users"
    id: int = Field(default=None, primary_key=True)
    email: str
    password: str
    user_type: UserType
