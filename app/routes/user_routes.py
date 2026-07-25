from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import get_users, create_user, get_user, update_user
from app.dependencies import get_db

router = APIRouter()

@router.get("/users", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/users", response_model=UserResponse)
def add_user(user : UserCreate, db: Session = Depends(get_db)):
    return create_user(db,user)

@router.get("/users/{user_id}", response_model = UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)
    

@router.put("/users/{user_id}", response_model = UserResponse)
def modify_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user)
   