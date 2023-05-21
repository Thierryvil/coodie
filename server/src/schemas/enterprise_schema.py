from typing import Optional

from sqlmodel import Field, SQLModel


class EnterpriseSchema(SQLModel, table=True):
    __tablename__: str = "enterprises"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = Field(index=True)
    description: str
