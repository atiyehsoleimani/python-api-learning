from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services import get_users, create_user, get_user, update_user
from app.dependencies import get_db
from app.services.user_service import delete_user

router = APIRouter(tags=["Users"])

@router.get("/users", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/users", response_model=UserResponse, status_code=201)
def add_user(user : UserCreate, db: Session = Depends(get_db)):
    return create_user(db,user)

@router.get("/users/{user_id}", response_model = UserResponse)
def read_user(user_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return get_user(db, user_id)
    

@router.put("/users/{user_id}", response_model = UserResponse)
def modify_user(user: UserUpdate, user_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return update_user(db, user_id, user)

@router.delete("/users/{user_id}", response_model = UserResponse)
def remove_user(user_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return delete_user(db, user_id)
