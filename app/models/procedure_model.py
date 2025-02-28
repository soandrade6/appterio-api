from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database import Base

class Procedure(Base):
    __tablename__ = "procedure"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    specimen_id = Column(UUID(as_uuid=True), ForeignKey("animal.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    status = Column(String, nullable=False, default="Pendiente")
    
    specimen = relationship("Animal", back_populates="procedures")
    user = relationship("User", back_populates="procedures")
   