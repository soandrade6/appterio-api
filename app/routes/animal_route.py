from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.animal_schema import AnimalCreate, AnimalResponse, AnimalDetailResponse, AnimalFamilyResponse, AnimalUpdate
from app.services.animal_service import create_animal, get_animal, get_animals_by_keeper, get_animals_by_researcher, get_animal_family, get_alive_animals, update_animal
import uuid

router = APIRouter(prefix="/animal", tags=["Animals"])


@router.post("/", response_model=AnimalResponse)
def create_animal_route(animal: AnimalCreate, db: Session = Depends(get_db)):
    return create_animal(db, animal)


@router.get("/detail/{id}", response_model=AnimalDetailResponse)
def get_animal_route(id: uuid.UUID, db: Session = Depends(get_db)):
    animal = get_animal(db, id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return animal

@router.get("/keeper/{id}", response_model=list[AnimalResponse])
def get_animals_by_keeper_route(id: uuid.UUID, db: Session = Depends(get_db)):
    return get_animals_by_keeper(db, id)

@router.get("/researcher/{id}", response_model=list[AnimalResponse])
def get_animals_by_researcher_route(id: uuid.UUID, db: Session = Depends(get_db)):
    return get_animals_by_researcher(db, id)

@router.get("/family/{id}", response_model=AnimalFamilyResponse)
def get_animal_family_route(id: uuid.UUID, db: Session = Depends(get_db)):
    return get_animal_family(db, id)

@router.get("/alive", response_model=list[AnimalResponse])
def get_alive_animals_route(db: Session = Depends(get_db)):
    return get_alive_animals(db)

@router.patch("/{id}", response_model=AnimalDetailResponse)
def update_animal_route(id: uuid.UUID, animal: AnimalUpdate, db: Session = Depends(get_db)):
    return update_animal(db, id, animal)
