from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.models.procedure_model import Procedure
from app.models.user_model import User, UserRole
from app.schemas.procedure_schema import ProcedureCreate

def create_procedure(db: Session, data: ProcedureCreate):
    try:
        new_procedure = Procedure(**data.dict())
        db.add(new_procedure)
        db.commit()
        db.refresh(new_procedure)
        return new_procedure
    except SQLAlchemyError as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail=f"Error al crear el procedimiento: {str(e)}")
    
def update_procedure_status(db: Session, id: str, status: str):
    try:
        procedure = db.query(Procedure).filter(Procedure.id == id).first()
        if not procedure:
            raise HTTPException(status_code=404, detail="Procedimiento no encontrado")
        procedure.status = status
        db.commit()
        db.refresh(procedure)
        return procedure
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar el procedimiento: {str(e)}")
    
    
def get_procedures_by_researcher(db: Session, user_id: str):
    # Validar si el usuario es un investigador
    user = db.query(User).filter(User.id == user_id, User.role == UserRole.investigador).first()
    if not user:
        raise HTTPException(status_code=403, detail="El usuario no tiene rol de investigador o no existe.")

    procedures = db.query(Procedure).filter(Procedure.user_id == user_id).all()
    if not procedures:
        raise HTTPException(status_code=404, detail="No se encontraron procedimientos para este investigador.")
    
    return procedures

def get_procedures_by_keeper(db: Session, user_id: str):
    # Validar si el usuario es un cuidador
    user = db.query(User).filter(User.id == user_id, User.role == UserRole.cuidador).first()
    if not user:
        raise HTTPException(status_code=403, detail="El usuario no tiene rol de cuidador o no existe.")

    procedures = db.query(Procedure).join(User, Procedure.user_id == User.id).filter(User.id == user_id).all()
    if not procedures:
        raise HTTPException(status_code=404, detail="No se encontraron procedimientos para este cuidador.")

    return procedures