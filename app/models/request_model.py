from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database import Base

class Request(Base):
    __tablename__ = "request"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    researcher_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    keeper_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    status = Column(String, nullable=False, default="Pendiente")
    
    researcher = relationship("User", foreign_keys=[researcher_id], back_populates="requests_researcher")
    keeper = relationship("User", foreign_keys=[keeper_id], back_populates="requests_keeper")
   