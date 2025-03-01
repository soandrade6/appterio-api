from pydantic import BaseModel, UUID4
# from app.schemas.animal_schema import AnimalProcedureResponse

class ProcedureCreate(BaseModel):
    title: str
    description: str
    specimen_id: UUID4
    user_id: UUID4
    status: str

class ProcedureResponse(ProcedureCreate):
    id: UUID4
    title: str
    description: str
    specimen_id: UUID4
    user_id: UUID4
    status: str

    class Config:
        from_attributes = True


class ProcedureUpdateStatus(BaseModel):
    status: str


# class ProcedureUser(BaseModel):
#     id: UUID4
#     title: str
#     description: str
#     specimen: AnimalProcedureResponse
#     status: str
