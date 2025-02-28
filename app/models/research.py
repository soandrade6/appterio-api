from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base

class Research(Base):
    __tablename__ = "research"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    specimen_id = Column(UUID(as_uuid=True), ForeignKey("animal.id"), nullable=False)
    researcher_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    status = Column(String, nullable=False, default="Abierta")
