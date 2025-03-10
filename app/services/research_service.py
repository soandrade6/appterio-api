from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.models.research_model import Research
from app.schemas.research_schema import ResearchCreate

def create_research(db: Session, data: ResearchCreate):
    try:
        new_research = Research(**data.dict())
        db.add(new_research)
        db.commit()
        db.refresh(new_research)
        return new_research
    except SQLAlchemyError as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail=f"Error al crear el la investigación: {str(e)}")
    
def update_research_status(db: Session, id: str, status: str):
    try:
        research = db.query(Research).filter(Research.id == id).first()
        if not research:
            raise HTTPException(status_code=404, detail="No se encontraron investigaciones")
        research.status = status
        db.commit()
        db.refresh(research)
        return research
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar la investigación: {str(e)}")
