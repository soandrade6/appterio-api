from pydantic import BaseModel, UUID4

class ResearchCreate(BaseModel):
    title: str
    description: str
    specimen_id: UUID4
    researcher_id: UUID4
    status: str

class ResearchResponse(ResearchCreate):
    title: str
    description: str
    specimen_id: UUID4
    researcher_id: UUID4
    status: str

    class Config:
        from_attributes = True
