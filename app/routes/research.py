from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.research import ResearchCreate, ResearchResponse, ResearchUpdateStatus
from app.services.research import create_research, update_research_status

router = APIRouter(prefix="/research", tags=["Research"])

@router.post("/", response_model=ResearchResponse)
def create_new_research(research: ResearchCreate, db: Session = Depends(get_db)):
    new_research = create_research(db, research)
    return new_research


@router.put("/{animal_id}", response_model=ResearchUpdateStatus)
def update_research(animal_id: str, update_data: ResearchUpdateStatus, db: Session = Depends(get_db)):
    return update_research_status(db, animal_id, update_data.status)
