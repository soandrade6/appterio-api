from pydantic import BaseModel, UUID4
from app.schemas.user_schema import UserResponse


class RequestCreate(BaseModel):
    title: str
    description: str
    researcher_id: UUID4
    keeper_id: UUID4
    status: str


class RequestResponse(RequestCreate):
    id: UUID4
    title: str
    description: str
    researcher_id: UUID4
    keeper_id: UUID4
    status: str

    class Config:
        from_attributes = True


class RequestUpdateStatus(BaseModel):
    status: str


class RequestResearchers(BaseModel):
    id: UUID4
    title: str
    description: str
    keeper: UserResponse
    status: str


class RequestKeepers(BaseModel):
    id: UUID4
    title: str
    description: str
    researcher: UserResponse
    status: str
