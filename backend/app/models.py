import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

""" properties to share """


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)


""" Properties to recive  by API on creation"""


class UserCreate(UserBase):
    password: str = Field(min_length=6, max_length=10)


class UserRegister(SQLModel):
    email: EmailStr = Field(max_length=255)
    username: str | None = Field(default=None, min_length=3, max_length=255)
    password: str = Field(min_length=6, max_length=10)
    full_name: str | None = Field(default=None, max_length=255)


""" Properties to update by API"""


class UserUpdate(UserBase):
    email: EmailStr | None = Field(default=None, max_length=255)
    password: str | None = Field(default=None, min_length=6, max_length=10)


class UserUpdateMe(SQLModel):
    full_name: str | None = Field(default=None, max_length=255)
    email: EmailStr | None = Field(default=None, max_length=255)


class UpdatePassword(SQLModel):
    current_password: str = Field(min_length=6, max_length=10)
    password: str = Field(min_length=6, max_length=10)


""" Databe  model table class name"""


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str = Field(min_length=6, max_length=10)


""" Properties to return by API"""


class UserPublic(SQLModel):
    id: uuid.UUID
    username: str | None = None


"""Payloads and Tokens"""


"""JSON"""


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


"""JWT Token"""


class TokenPLayLoad(SQLModel):
    sub: str | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str = Field(min_length=6, max_length=10)
