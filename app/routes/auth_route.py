from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user_schema import Token 
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    print("holo")
    user = auth_service.authenticate_user(db, form_data.username, form_data.password)
    print("aca")

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_service.create_token_for_user(user)
    return {"access_token": access_token, "token_type": "bearer"}
