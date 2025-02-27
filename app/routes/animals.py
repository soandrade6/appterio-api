from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.animal import AnimalCreate, AnimalResponse
from app.services.animal import create_animal, get_animal
import uuid

router = APIRouter(prefix="/animales", tags=["Animales"])


@router.post("/", response_model=AnimalResponse)
def create_animal_route(animal: AnimalCreate, db: Session = Depends(get_db)):
    return create_animal(db, animal)


@router.get("/{animal_id}", response_model=AnimalResponse)
def get_animal_route(animal_id: uuid.UUID, db: Session = Depends(get_db)):
    animal = get_animal(db, animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return animal
