from typing import List

from pydantic import BaseModel, validator

ALLOWED_SENIORITY = {"junior", "pleno", "senior"}
ALLOWED_LOCATION = {"remoto", "hibrido", "home office"}
ALLOWED_REGIME = {"clt", "pj"}


class Job(BaseModel):
    title: str
    description: str
    seniority: List[str]
    location: List[str]
    regime: List[str]

    @classmethod
    def validate_string_non_blank(cls, value, field_name):
        if not value.strip():
            raise ValueError(f"{field_name.capitalize()} must not be blank.")
        return value

    @validator("title")
    def validate_title(cls, v):
        return cls.validate_string_non_blank(v, "title")

    @validator("description")
    def validate_description(cls, v):
        return cls.validate_string_non_blank(v, "description")

    @validator("seniority")
    def validate_seniority(cls, v):
        if not v:
            raise ValueError("Seniority must not be empty.")
        invalid_seniority = set(v) - ALLOWED_SENIORITY
        if invalid_seniority:
            invalid_values = ", ".join(invalid_seniority)
            allowed_values = ", ".join(ALLOWED_SENIORITY)
            raise ValueError(
                f"Invalid seniority values: {invalid_values}. "
                f"Allowed values are: {allowed_values}."
            )
        return v

    @validator("location")
    def validate_location(cls, v):
        if not v:
            raise ValueError("Location must not be empty.")
        invalid_location = set(v) - {"remoto", "hibrido", "home office"}
        if invalid_location:
            invalid_values = ", ".join(invalid_location)
            allowed_values = ", ".join(ALLOWED_LOCATION)
            raise ValueError(
                f"Invalid location values: {invalid_values}. "
                f"Allowed values are: {allowed_values}."
            )
        return v

    @validator("regime")
    def validate_regime(cls, v):
        if not v:
            raise ValueError("Regime must not be empty.")
        invalid_regime = set(v) - ALLOWED_REGIME
        if invalid_regime:
            invalid_values = ", ".join(invalid_regime)
            allowed_values = ", ".join(ALLOWED_REGIME)
            raise ValueError(
                f"Invalid regime values: {invalid_values}. "
                f"Allowed values are: {allowed_values}."
            )
        return v
