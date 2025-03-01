from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from uuid import UUID
from app.schemas.request_schema import (
    RequestCreate,
    RequestResponse,
    RequestKeepers,
    RequestResearchers,
    RequestUpdateStatus
)
from app.services.request_service import (
    create_request,
    update_request_status,
    get_request_by_keeper,
    get_requets_by_researcher
)


router = APIRouter(prefix="/request", tags=["Request"])


@router.post("/", response_model=RequestResponse)
def create_new_request(research: RequestCreate, db: Session = Depends(get_db)):
    new_request = create_request(db, research)
    return new_request


@router.put("/{id}", response_model=RequestUpdateStatus)
def update_request(
    id: str, data: RequestUpdateStatus, db: Session = Depends(get_db)
):
    return update_request_status(db, id, data.status)


@router.get("/researcher/{user_id}", response_model=List[RequestResearchers])
def get_researcher_request(user_id: UUID, db: Session = Depends(get_db)):
    return get_requets_by_researcher(db, user_id)

@router.get("/keeper/{user_id}", response_model=List[RequestKeepers])
def get_keeper_request(user_id: UUID, db: Session = Depends(get_db)):
    return get_request_by_keeper(db, user_id)
