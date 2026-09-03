from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import Dict, Any, Optional
from app.core.security import get_password_hash, verify_password, create_access_token, decode_token

router = APIRouter()

# In-memory user store for starter prototype
USERS_DB: Dict[str, Dict[str, Any]] = {}

class UserSignUp(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: Dict[str, Any]

@router.post("/signup", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def signup(payload: UserSignUp):
    """Registers a new student account"""
    if payload.email in USERS_DB:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this email address already exists."
        )

    user_record = {
        "id": f"usr_{len(USERS_DB) + 1}",
        "name": payload.name,
        "email": payload.email,
        "hashed_password": get_password_hash(payload.password),
        "progress_percent": 0
    }
    USERS_DB[payload.email] = user_record

    token = create_access_token(subject=user_record["id"])
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {"id": user_record["id"], "name": user_record["name"], "email": user_record["email"]}
    }

@router.post("/login", response_model=TokenResponse)
def login(payload: UserLogin):
    """Authenticates student and returns a signed JWT bearer token"""
    user = USERS_DB.get(payload.email)
    if not user or not verify_password(payload.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )

    token = create_access_token(subject=user["id"])
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {"id": user["id"], "name": user["name"], "email": user["email"]}
    }
