from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.sql import func
from app.database import Base
import enum

class UserRole(enum.Enum):
    cuidador = "cuidador"
    investigador = "investigador"
    administrador = "administrador"
    
class User(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    contrasena = Column(String, nullable=False)
    rol = Column(Enum(UserRole), nullable=False)
    fecha_registro = Column(DateTime, nullable=False, server_default=func.now())

    animales = relationship("Animal", back_populates="cuidador")
