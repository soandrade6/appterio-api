from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserCreate, UserEdit
from app.core.security import hash_password
import uuid


def create_user(db: Session, user_data: UserCreate | UserEdit):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado. Intente con otro email.")
    new_user = User(
        id_usuario=uuid.uuid4(),
        nombre=user_data.nombre,
        email=user_data.email,
        contrasena=hash_password(user_data.contrasena),
        rol=user_data.rol
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, user_id: uuid.UUID):
    return db.query(User).filter(User.id_usuario == user_id).first()


def get_all_users(db: Session):
    return db.query(User).all()


def get_all_users_by_role(db: Session, role: str):
    return db.query(User).filter(User.rol == role).all()


def put_user(db: Session, user_id: uuid.UUID, user_data: UserEdit):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: uuid.UUID):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"ok": True}
