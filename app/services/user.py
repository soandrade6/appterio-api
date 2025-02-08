from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserCreate
import uuid

def create_user(db: Session, user_data: UserCreate):
    
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado. Intente con otro email.")
    new_user = User(
        id_usuario=uuid.uuid4(),
        nombre=user_data.nombre,
        email=user_data.email,
        contrasena=user_data.contrasena, 
        rol=user_data.rol
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: uuid.UUID):
    return db.query(User).filter(User.id_usuario == user_id).first()
