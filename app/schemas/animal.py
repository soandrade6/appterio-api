from pydantic import BaseModel
from uuid import UUID
from datetime import date

class AnimalCreate(BaseModel):
    name: str
    specie: str
    health_status: str
    weight: float
    date_birth: date
    origin: str
    family: str
    diet: str
    last_observations: str
    clinical_signs: str
    vaccines: str
    parent1Id: str
    parent2Id: str
    keeperId: UUID | None = None

class AnimalResponse(BaseModel):
    id: UUID
    name: str
    specie: str

    class Config:
        from_attributes = True
