from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from uuid import UUID
from app.schemas.procedure_schema import (
    ProcedureCreate,
    ProcedureResponse,
    ProcedureUpdateStatus,
)
from app.services.procedure_service import (
    create_procedure,
    update_procedure_status,
    get_procedures_by_keeper,
    get_procedures_by_researcher,
)


router = APIRouter(prefix="/procedure", tags=["Procedure"])


@router.post("/", response_model=ProcedureResponse)
def create_new_procedure(research: ProcedureCreate, db: Session = Depends(get_db)):
    new_procedure = create_procedure(db, research)
    return new_procedure


@router.put("/{id}", response_model=ProcedureUpdateStatus)
def update_procedure(
    id: str, data: ProcedureUpdateStatus, db: Session = Depends(get_db)
):
    return update_procedure_status(db, id, data.status)


@router.get("/researcher/{user_id}", response_model=List[ProcedureResponse])
def get_researcher_procedures(user_id: UUID, db: Session = Depends(get_db)):
    return get_procedures_by_researcher(db, user_id)

@router.get("/keeper/{user_id}", response_model=List[ProcedureResponse])
def get_keeper_procedures(user_id: UUID, db: Session = Depends(get_db)):
    return get_procedures_by_keeper(db, user_id)
