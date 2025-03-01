from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    cuidador = "cuidador"
    investigador = "investigador"
    administrador = "administrador"


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRole


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: UserRole
    registration_date: datetime

    class Config:
        from_attributes = True


class UserEdit(BaseModel):
    name: str
    email: EmailStr
    role: UserRole

class Token(BaseModel):
    access_token: str
    token_type: str

