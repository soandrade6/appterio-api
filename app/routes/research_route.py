from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.research_schema import ResearchCreate, ResearchResponse, ResearchUpdateStatus
from app.services.research_service import create_research, update_research_status

router = APIRouter(prefix="/research", tags=["Research"])

@router.post("/", response_model=ResearchResponse)
def create_new_research(research: ResearchCreate, db: Session = Depends(get_db)):
    new_research = create_research(db, research)
    return new_research


@router.put("/{id}", response_model=ResearchUpdateStatus)
def update_research(id: str, update_data: ResearchUpdateStatus, db: Session = Depends(get_db)):
    return update_research_status(db, id, update_data.status)
