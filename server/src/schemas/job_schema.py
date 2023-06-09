from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class JobSchema(SQLModel, table=True):
    __tablename__: str = "jobs"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(sa_column_kwargs={"nullable": False})
    description: str = Field(sa_column_kwargs={"nullable": False})
    seniority: str = Field()
    location: str = Field()
    regime: str = Field()
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    enterprise_id: Optional[int] = Field(
        default=None,
        foreign_key="users.id",
    )
