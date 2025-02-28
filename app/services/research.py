from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.models.research import Research
from app.schemas.research import ResearchCreate

def create_research(db: Session, research_data: ResearchCreate):
    try:
        new_research = Research(**research_data.dict())
        db.add(new_research)
        db.commit()
        db.refresh(new_research)
        return new_research
    except SQLAlchemyError as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail=f"Error al crear el la investigación: {str(e)}")
