from pydantic import BaseModel


class Enterprise(BaseModel):
    name: str
    description: str
