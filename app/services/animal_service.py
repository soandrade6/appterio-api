from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.models.user_model import UserRole
from app.models.animal_model import Animal, AnimalStatus
from app.models.detail_model import Diet, LastObservations, ClinicalSigns, Vaccines
from app.models.research_model import Research
from app.schemas.animal_schema import AnimalCreate, AnimalUpdate
from app.schemas.procedure_schema import ProcedureResponse
from app.schemas.research_schema import ResearchResponse
from app.services.user_service import get_user
from datetime import date
import uuid


def create_animal(db: Session, data: AnimalCreate):
    if data.keeper_id:
        keeper = get_user(db, data.keeper_id)
        if not keeper:
            raise HTTPException(status_code=404, detail="Cuidador no encontrado")

    try:
        new_animal = Animal(
            id=uuid.uuid4(),
            name=data.name,
            species=data.species,
            sex=data.sex,
            health_status=data.health_status,
            weight=data.weight,
            date_birth=data.date_birth,
            age=data.age,
            origin=data.origin,
            family=data.family,
            parent1_id=data.parent1_id,
            parent2_id=data.parent2_id,
            keeper_id=data.keeper_id,
        )

        db.add(new_animal)
        db.commit()
        db.refresh(new_animal)

        if data.diet:
            diet = Diet(id=uuid.uuid4(), description=data.diet, animal_id=new_animal.id)
            db.add(diet)

        if data.last_observations:
            last_observations = LastObservations(
                id=uuid.uuid4(),
                description=data.last_observations,
                animal_id=new_animal.id,
            )
            db.add(last_observations)

        if data.clinical_signs:
            clinical_signs = ClinicalSigns(
                id=uuid.uuid4(),
                description=data.clinical_signs,
                animal_id=new_animal.id,
            )
            db.add(clinical_signs)

        if data.vaccines:
            vaccines = Vaccines(
                id=uuid.uuid4(), description=data.vaccines, animal_id=new_animal.id
            )
            db.add(vaccines)

        db.commit()
        return new_animal

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Error al crear el animal: {str(e)}"
        )


def get_animal(db: Session, id: uuid.UUID):
    try:
        animal = db.query(Animal).filter(Animal.id == id).first()
        if not animal:
            raise HTTPException(status_code=404, detail="Animal no encontrado")

        today = date.today()
        age = (
            (today.year - animal.date_birth.year) * 12
            + (today.month - animal.date_birth.month)
            if animal.date_birth
            else animal.age
        )

        return {
            "id": animal.id,
            "name": animal.name,
            "species": animal.species,
            "sex": animal.sex.name,
            "health_status": animal.health_status.name,
            "weight": animal.weight,
            "age": age,
            "origin": animal.origin,
            "family": animal.family,
            "details": {
                "diet": {
                    "last_update": (
                        animal.diet.last_update_date.strftime("%d/%m/%Y")
                        if animal.diet
                        else None
                    ),
                    "description": animal.diet.description if animal.diet else None,
                },
                "last_observations": {
                    "last_update": (
                        animal.last_observations.last_update_date.strftime("%d/%m/%Y")
                        if animal.last_observations
                        else None
                    ),
                    "description": (
                        animal.last_observations.description
                        if animal.last_observations
                        else None
                    ),
                },
                "clinical_signs": {
                    "last_update": (
                        animal.clinical_signs.last_update_date.strftime("%d/%m/%Y")
                        if animal.clinical_signs
                        else None
                    ),
                    "description": (
                        animal.clinical_signs.description
                        if animal.clinical_signs
                        else None
                    ),
                },
                "vaccines": {
                    "last_update": (
                        animal.vaccines.last_update_date.strftime("%d/%m/%Y")
                        if animal.vaccines
                        else None
                    ),
                    "description": (
                        animal.vaccines.description if animal.vaccines else None
                    ),
                },
            },
            "procedures": [
                {
                    "id": procedure.id,
                    "title": procedure.title,
                    "description": procedure.description,
                    "status": procedure.status,
                }
                for procedure in animal.procedures
            ],
            "researches": [
                {
                    "id": research.id,
                    "title": research.title,
                    "description": research.description,
                    "status": research.status,
                }
                for research in animal.researches
            ],
            "parent1_id": animal.parent1_id,
            "parent2_id": animal.parent2_id,
            "keeper_id": animal.keeper_id,
        }

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener detalles del animal: {str(e)}"
        )


def get_animals_by_keeper(db: Session, id: uuid.UUID):
    try:
        keeper = get_user(db, id)
        if not keeper or keeper.role != UserRole.cuidador:
            raise HTTPException(status_code=404, detail="Cuidador no encontrado")

        return keeper.animals
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener los animales del cuidador: {str(e)}",
        )


def get_animals_by_researcher(db: Session, id: uuid.UUID):
    try:
        researcher = get_user(db, id)
        if not researcher or researcher.role != UserRole.investigador:
            raise HTTPException(status_code=404, detail="Investigador no encontrado")

        research_studies = (
            db.query(Research).filter(Research.researcher_id == researcher.id).all()
        )
        if not research_studies:
            return []

        animals = (
            db.query(Animal)
            .join(Research)
            .filter(Research.researcher_id == researcher.id)
            .all()
        )

        return animals

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener los animales del investigador: {str(e)}",
        )


def get_animal_family(db: Session, id: uuid.UUID):
    try:
        animal = db.query(Animal).filter(Animal.id == id).first()
        if not animal:
            raise HTTPException(status_code=404, detail="Animal no encontrado")

        parent1 = animal.parent1 if animal.parent1_id else None
        parent2 = animal.parent2 if animal.parent2_id else None

        offspring = (
            db.query(Animal)
            .filter((Animal.parent1_id == animal.id) | (Animal.parent2_id == animal.id))
            .all()
        )

        return {
            "parents": {
                "parent1": (
                    {
                        "id": parent1.id,
                        "name": parent1.name,
                        "species": parent1.species,
                        "sex": parent1.sex.name,
                        "health_status": parent1.health_status.name,
                    }
                    if parent1
                    else None
                ),
                "parent2": (
                    {
                        "id": parent2.id,
                        "name": parent2.name,
                        "species": parent2.species,
                        "sex": parent2.sex.name,
                        "health_status": parent2.health_status.name,
                    }
                    if parent2
                    else None
                ),
            },
            "offspring": [
                {
                    "id": young.id,
                    "name": young.name,
                    "species": young.species,
                    "sex": young.sex.name,
                    "health_status": young.health_status.name,
                }
                for young in offspring
            ],
        }

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener familia del animal: {str(e)}"
        )


def get_alive_animals(db: Session):
    try:
        return (
            db.query(Animal)
            .filter(
                Animal.health_status.in_([AnimalStatus.SALUDABLE, AnimalStatus.CUIDADO])
            )
            .all()
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener los animales vivos: {str(e)}"
        )


def update_animal(db: Session, id: uuid.UUID, data: AnimalUpdate):
    try:
        animal = db.query(Animal).filter(Animal.id == id).first()
        if not animal:
            raise HTTPException(status_code=404, detail="Animal no encontrado")

        for field, value in data.dict(exclude_unset=True).items():
            if field in ["health_status", "weight", "age", "keeper_id"]:
                setattr(animal, field, value)

        if data.diet:
            if animal.diet:
                animal.diet.description = data.diet
                animal.diet.last_update_date = date.today()
            else:
                new_diet = Diet(
                    id=uuid.uuid4(),
                    description=data.diet,
                    animal_id=animal.id,
                )
                db.add(new_diet)

        if data.last_observations:
            if animal.last_observations:
                animal.last_observations.description = data.last_observations
                animal.last_observations.last_update_date = date.today()
            else:
                new_last_observations = LastObservations(
                    id=uuid.uuid4(),
                    description=data.last_observations,
                    animal_id=animal.id,
                )
                db.add(new_last_observations)

        if data.clinical_signs:
            if animal.clinical_signs:
                animal.clinical_signs.description = data.clinical_signs
                animal.clinical_signs.last_update_date = date.today()
            else:
                new_clinical_signs = ClinicalSigns(
                    id=uuid.uuid4(),
                    description=data.clinical_signs,
                    animal_id=animal.id,
                )
                db.add(new_clinical_signs)

        if data.vaccines:
            if animal.vaccines:
                animal.vaccines.description = data.vaccines
                animal.vaccines.last_update_date = date.today()
            else:
                new_vaccines = Vaccines(
                    id=uuid.uuid4(),
                    description=data.vaccines,
                    animal_id=animal.id,
                )
                db.add(new_vaccines)

        db.commit()
        db.refresh(animal)

        return get_animal(db, animal.id)

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500, detail=f"Error al actualizar el animal: {str(e)}"
        )
