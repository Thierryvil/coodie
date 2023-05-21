from typing import Optional, Set

from sqlmodel import Field, SQLModel


class JobSchema(SQLModel, table=True):
    __tablename__: str = "jobs"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(sa_column_kwargs={"nullable": False})
    description: str = Field(sa_column_kwargs={"nullable": False})
    seniority: Set[str] = Field(default=set())
    location: Set[str] = Field(default=set())
    regime: Set[str] = Field(default=set())
    enterprise_id: Optional[int] = Field(
        default=None,
        foreign_key="enterprises.id",
    )
