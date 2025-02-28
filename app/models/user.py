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
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    registration_date = Column(DateTime, nullable=False, server_default=func.now())

    animals = relationship("Animal", back_populates="keeper")
