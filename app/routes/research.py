from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.research import ResearchCreate, ResearchResponse
from app.services.research import create_research

router = APIRouter(prefix="/research", tags=["Research"])

@router.post("/", response_model=ResearchResponse)
def create_new_research(research: ResearchCreate, db: Session = Depends(get_db)):
    new_research = create_research(db, research)
    return new_research
