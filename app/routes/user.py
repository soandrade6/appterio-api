from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserEdit
from app.services.user import create_user, get_user, get_all_users, get_all_users_by_role, update_user, delete_user
import uuid

router = APIRouter(prefix="/user", tags=["User"])


# Crear un usuario
@router.post("/", response_model=UserResponse)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


# Obtener un usuario por id
@router.get("/{user_id}", response_model=UserResponse)
def get_user_route(user_id: uuid.UUID, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


# Obtener todos los usuarios y filtrar por rol si se especifica
@router.get("/", response_model=list[UserResponse])
def get_users(role: str | None = None, db: Session = Depends(get_db)):
    if role:
        return get_all_users_by_role(db, role)
    return get_all_users(db)


# Actualizar un usuario
@router.put("/{user_id}", response_model=UserResponse)
def put_user_route(user_id: uuid.UUID, user: UserEdit, db: Session = Depends(get_db)):
    return update_user(db, user_id, user)


@router.delete("/{user_id}")
def delete_user_route(user_id: uuid.UUID, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
