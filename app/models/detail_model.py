from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.database import Base

class Diet(Base):
    __tablename__ = "diet"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    last_update_date = Column(Date, nullable=False, server_default=func.now())
    description = Column(String, nullable=False)

    animal_id = Column(UUID(as_uuid=True), ForeignKey("animal.id"), unique=True)
    animal = relationship("Animal", back_populates="diet")

class LastObservations(Base):
    __tablename__ = "last_observations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    last_update_date = Column(Date, nullable=False, server_default=func.now())
    description = Column(String, nullable=False)

    animal_id = Column(UUID(as_uuid=True), ForeignKey("animal.id"), unique=True)
    animal = relationship("Animal", back_populates="last_observations")

class ClinicalSigns(Base):
    __tablename__ = "clinical_signs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    last_update_date = Column(Date, nullable=False, server_default=func.now())
    description = Column(String, nullable=False)

    animal_id = Column(UUID(as_uuid=True), ForeignKey("animal.id"), unique=True)
    animal = relationship("Animal", back_populates="clinical_signs")

class Vaccines(Base):
    __tablename__ = "vaccines"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    last_update_date = Column(Date, nullable=False, server_default=func.now())
    description = Column(String, nullable=False)

    animal_id = Column(UUID(as_uuid=True), ForeignKey("animal.id"), unique=True)
    animal = relationship("Animal", back_populates="vaccines")
