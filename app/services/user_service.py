from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserEdit
from app.core.security import hash_password
import uuid


def create_user(db: Session, data: UserCreate | UserEdit):
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado. Intente con otro email.")
    new_user = User(
        id=uuid.uuid4(),
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        role=data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, id: uuid.UUID):
    return db.query(User).filter(User.id == id).first()


def get_all_users(db: Session):
    return db.query(User).all()


def get_all_users_by_role(db: Session, role: str):
    return db.query(User).filter(User.role == role).all()


def update_user(db: Session, id: uuid.UUID, data: UserEdit):
    user = get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, id: uuid.UUID):
    user = get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"ok": True}
