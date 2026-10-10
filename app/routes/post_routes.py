from fastapi import APIRouter, Depends, status, Query, Path
from sqlalchemy.orm import Session 

from app.dependencies import get_db
from app.exceptions import PostNotFoundException, UserNotFoundException
from app.schemas import PostCreate, PostUpdate, PostResponse
from app.services import post_service

router = APIRouter(tags=["posts"])

@router.get("/users/{user_id}/posts", response_model=list[PostResponse])
def list_posts(user_id: int = Path(..., gt=0), skip: int = Query(0, ge=0),limit: int = Query(100, ge=1, le=100), db: Session = Depends(get_db)):
    return post_service.get_posts_by_user(db, skip, limit, user_id)

@router.post("/users/{user_id}/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, user_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return post_service.create_post(db, post=post, user_id=user_id)

@router.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return post_service.get_post(db, post_id=post_id)

@router.patch("/posts/{post_id}", response_model=PostResponse)
def update_post(post: PostUpdate, post_id: int = Path(..., gt=0),  db: Session = Depends(get_db)):
    return post_service.update_post(db, post_id=post_id, post=post)

@router.delete("/posts/{post_id}", response_model=PostResponse)
def delete_post(post_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return post_service.delete_post(db, post_id=post_id)



