from pydantic import BaseModel
from uuid import UUID
from datetime import date
from enum import Enum

class AnimalSex(str, Enum):
    HEMBRA = "HEMBRA"
    MACHO = "MACHO"

class AnimalStatus(str, Enum):
    DECESO = "DECESO"
    CUIDADO = "CUIDADO"
    SALUDABLE = "SALUDABLE"

class ProcedureAndResearchDetailResponse(BaseModel):
    id: UUID
    title: str
    description: str
    status: str

class AnimalCreate(BaseModel):
    name: str
    species: str
    sex: AnimalSex
    health_status: AnimalStatus
    weight: float
    date_birth: date | None = None
    age: int
    origin: str
    family: str
    diet: str | None = None
    last_observations: str | None = None
    clinical_signs: str | None = None
    vaccines: str | None = None
    parent1_id: UUID | None = None
    parent2_id: UUID | None = None
    keeper_id: UUID | None = None


class AnimalResponse(BaseModel):
    id: UUID
    sex: AnimalSex
    species: str
    family: str
    health_status: AnimalStatus

    class Config:
        from_attributes = True

class AnimalDetailResponse(BaseModel):
    id: UUID
    name: str
    species: str
    sex: AnimalSex
    health_status: AnimalStatus
    weight: float
    age: int
    origin: str
    family: str
    details: dict
    procedures: list[ProcedureAndResearchDetailResponse] = []
    researches: list[ProcedureAndResearchDetailResponse] = []
    parent1_id: UUID | None = None
    parent2_id: UUID | None = None
    keeper_id: UUID | None = None

    class Config:
        from_attributes = True

    
class AnimalFamilyResponse(BaseModel):
    parents: dict
    offspring: list[AnimalResponse]


class AnimalUpdate(BaseModel):
    health_status: AnimalStatus | None = None
    weight: float | None = None
    age: int | None = None
    diet: str | None = None
    last_observations: str | None = None
    clinical_signs: str | None = None
    vaccines: str | None = None
    keeper_id: UUID | None = None
