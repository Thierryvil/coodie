from typing import Optional, Set

from pydantic import BaseModel, validator


class Job(BaseModel):
    id: Optional[int]
    title: str
    description: str
    seniority: Set[str]
    location: Set[str]
    regime: Set[str]

    @validator("title")
    def title_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Title must not be blank.")
        return v

    @validator("description")
    def description_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Description must not be blank.")
        return v

    @validator("seniority")
    def validate_seniority(cls, v):
        if not v:
            raise ValueError("Empty seniority")
        invalid_seniority = v - {"junior", "pleno", "senior"}
        if invalid_seniority:
            raise ValueError(f"Invalid seniority: {invalid_seniority}")
        return v

    @validator("location")
    def validate_location(cls, v):
        if not v:
            raise ValueError("Empty location")

        invalid_location = v - {"remoto", "hibrido", "presencial"}
        if invalid_location:
            raise ValueError(f"Invalid location: {invalid_location}")
        return v

    @validator("regime")
    def validate_regime(cls, v):
        if not v:
            raise ValueError("Empty regime")

        invalid_regime = v - {"clt", "pj"}
        if invalid_regime:
            raise ValueError(f"Invalid regime: {invalid_regime}")
        return v
