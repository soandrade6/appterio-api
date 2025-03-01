from sqlalchemy.orm import Session
from app.services.user_service import get_user_by_email
from app.core import security
from datetime import timedelta

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not security.verify_password(password, user.password):
        return None
    return user

def create_token_for_user(user, expires_minutes: int = None):
    expires_delta = timedelta(minutes=expires_minutes if expires_minutes else security.JWT_EXPIRATION_MINUTES)
    token = security.create_access_token(data={"sub": str(user.id)}, expires_delta=expires_delta)
    return token