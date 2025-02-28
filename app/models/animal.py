from sqlalchemy import Column, String, Float, ForeignKey, Date, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database import Base
import enum

class AnimalSex(enum.Enum):
    HEMBRA = "HEMBRA"
    MACHO = "MACHO"

class AnimalStatus(enum.Enum):
    DECESO = "DECESO"
    CUIDADO = "CUIDADO"
    SALUDABLE = "SALUDABLE"

class Animal(Base):
    __tablename__ = "animal"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    sex = Column(Enum(AnimalSex), nullable=False)
    health_status = Column(Enum(AnimalStatus), nullable=False)
    weight = Column(Float, nullable=False)
    date_birth = Column(Date, nullable=True)
    age = Column(Integer, nullable=False)
    origin = Column(String, nullable=False)
    family = Column(String, nullable=False)

    parent1_id = Column(UUID(as_uuid=True), ForeignKey("animal.id"), nullable=True)
    parent2_id = Column(UUID(as_uuid=True), ForeignKey("animal.id"), nullable=True)
    keeper_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True)

    keeper = relationship("User", back_populates="animals")
    diet = relationship("Diet", back_populates="animal", uselist=False)
    last_observations = relationship(
        "LastObservations",
        back_populates="animal",
        uselist=False
    )
    clinical_signs = relationship(
        "ClinicalSigns",
        back_populates="animal",
        uselist=False
        )
    vaccines = relationship("Vaccines", back_populates="animal", uselist=False)
    parent1 = relationship("Animal", remote_side=[id], foreign_keys=[parent1_id])
    parent2 = relationship("Animal", remote_side=[id], foreign_keys=[parent2_id])
