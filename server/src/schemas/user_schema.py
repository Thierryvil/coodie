from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    email: str
    password: str
    is_active: bool = True


class CandidateCreate(UserBase):
    full_name: str


class CompanyCreate(UserBase):
    company_name: str


class UserSchema(SQLModel, table=True):
    __tablename__: str = "users"

    id: int = Field(default=None, primary_key=True)
    email: str
    password: str
    is_active: bool = True


class CandidateSchema(UserSchema, table=True):
    name: str
    is_candidate: bool = True


class EnterpriseSchema(UserSchema, table=True):
    name: str
    is_company: bool = True
