from sqlalchemy.orm import Session
from app.models.animal import Animal
from app.schemas.animal import AnimalCreate
import uuid

def create_animal(db: Session, animal_data: AnimalCreate):
    new_animal = Animal(
        id_animal=uuid.uuid4(),
        nombre=animal_data.nombre,
        especie=animal_data.especie,
        estado_salud=animal_data.estado_salud,
        peso=animal_data.peso,
        fecha_nacimiento=animal_data.fecha_nacimiento,
        origen=animal_data.origen,
        id_cuidador=animal_data.id_cuidador
    )
    db.add(new_animal)
    db.commit()
    db.refresh(new_animal)
    return new_animal

def get_animal(db: Session, animal_id: uuid.UUID):
    return db.query(Animal).filter(Animal.id_animal == animal_id).first()
