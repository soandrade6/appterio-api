from pydantic import BaseModel
from uuid import UUID
from datetime import date

class AnimalCreate(BaseModel):
    nombre: str
    especie: str
    estado_salud: str
    peso: float
    fecha_nacimiento: date
    origen: str
    id_cuidador: UUID | None = None

class AnimalResponse(BaseModel):
    id_animal: UUID
    nombre: str
    especie: str
    estado_salud: str
    peso: float
    fecha_nacimiento: date
    origen: str

    class Config:
        from_attributes = True
