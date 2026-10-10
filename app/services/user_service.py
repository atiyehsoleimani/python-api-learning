from app.models.user import User
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate
from app.exceptions.user_exceptions import UserNotFoundException

def get_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise UserNotFoundException(user_id=user_id)
    return user

def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = get_user(db, user_id)
    

    db_user.name = user.name
    
    db_user.email = user.email

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)

    db.delete(db_user)
    db.commit()
    return db_user