from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.models.animal_model import Animal
from app.schemas.animal_schema import AnimalCreate
import uuid

def create_animal(db: Session, data: AnimalCreate):
    try:
        new_animal = Animal(
            id=uuid.uuid4(),
            name=data.name,
            specie=data.specie,
            health_status=data.health_status,
            weight=data.weight,
            date_birth=data.date_birth,
            origin=data.origin,
            family=data.family,
            diet=data.diet,
            last_observations=data.last_observations,
            clinical_signs=data.clinical_signs,
            vaccines=data.vaccines,
            parent1Id=data.parent1Id,
            parent2Id=data.parent2Id,
            keeperId=data.keeperId
        )
        db.add(new_animal)
        db.commit()
        db.refresh(new_animal)
        return new_animal
    except SQLAlchemyError as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail=f"Error al crear el animal: {str(e)}")

def get_animal(db: Session, id: uuid.UUID):
    return db.query(Animal).filter(Animal.id == id).first()
