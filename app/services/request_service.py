from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.models.request_model import Request
from app.models.user_model import User, UserRole
from app.schemas.request_schema import RequestCreate

def create_request(db: Session, data: RequestCreate):
    try:
        new_request = Request(**data.dict())
        db.add(new_request)
        db.commit()
        db.refresh(new_request)
        return new_request
    except SQLAlchemyError as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail=f"Error al crear la solicitud: {str(e)}")
    
def update_request_status(db: Session, id: str, status: str):
    try:
        request = db.query(Request).filter(Request.id == id).first()
        if not request:
            raise HTTPException(status_code=404, detail="Solicitud no encontrada")
        request.status = status
        db.commit()
        db.refresh(request)
        return request
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar la solicitud: {str(e)}")
    
    
def get_requets_by_researcher(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id, User.role == UserRole.investigador).first()
    if not user:
        raise HTTPException(status_code=403, detail="El usuario no tiene rol de investigador o no existe.")

    request = db.query(Request).filter(Request.researcher_id == user_id).all()
    if not request:
        raise HTTPException(status_code=404, detail="No se encontraron solicitudes para este investigador.")
    
    return request

def get_request_by_keeper(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id, User.role == UserRole.cuidador).first()
    if not user:
        raise HTTPException(status_code=403, detail="El usuario no tiene rol de cuidador o no existe.")

    request = db.query(Request).join(User, Request.keeper_id == User.id).filter(User.id == user_id).all()
    if not request:
        raise HTTPException(status_code=404, detail="No se encontraron procedimientos para este cuidador.")

    return request