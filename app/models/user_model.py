from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.sql import func
from app.database import Base
import enum
from app.models.request_model import Request

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
    researches = relationship("Research", back_populates="researcher")
    procedures = relationship("Procedure", back_populates="user")

    requests_researcher = relationship("Request", foreign_keys=[Request.researcher_id], back_populates="researcher")
    requests_keeper = relationship("Request", foreign_keys=[Request.keeper_id], back_populates="keeper")
