from sqlalchemy import Column, String, Float, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database import Base

class Animal(Base):
    __tablename__ = "animal"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    specie = Column(String, nullable=False)
    health_status = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    date_birth = Column(Date, nullable=False)
    origin = Column(String, nullable=False)
    family = Column(String, nullable=False)
    diet = Column(String, nullable=False)
    last_observations = Column(String, nullable=False)
    clinical_signs = Column(String, nullable=False)
    vaccines = Column(String, nullable=False)
    parent1_id = Column(String, nullable=False)
    parent2_id = Column(String, nullable=False)
    keeper_id= Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True)

    keeper = relationship("User", back_populates="animals")
    procedures = relationship("Procedure", back_populates="specimen")
    researches = relationship("Research", back_populates="specimen")
    
