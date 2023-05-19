from pydantic import BaseModel


class Enterprise(BaseModel):
    id: int
    name: str
    description: str
