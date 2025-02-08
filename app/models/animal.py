from sqlalchemy import Column, String, Float, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database import Base

class Animal(Base):
    __tablename__ = "animales"

    id_animal = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String, nullable=False)
    especie = Column(String, nullable=False)
    estado_salud = Column(String, nullable=False)
    peso = Column(Float, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    origen = Column(String, nullable=False)
    id_cuidador = Column(UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=True)

    cuidador = relationship("User", back_populates="animales")
