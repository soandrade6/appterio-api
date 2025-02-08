from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    cuidador = "cuidador"
    investigador = "investigador"
    administrador = "administrador"

class UserCreate(BaseModel):
    nombre: str
    email: EmailStr
    contrasena: str
    rol: UserRole

class UserResponse(BaseModel):
    id_usuario: UUID
    nombre: str
    email: EmailStr
    rol: UserRole
    fecha_registro: datetime

    class Config:
        from_attributes = True
