from sqlalchemy.orm import Session
from app.models import Post, User
from app.schemas import PostCreate, PostUpdate
from app.exceptions import PostNotFoundException, UserNotFoundException

def get_post(db: Session, post_id: int) -> Post:
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise PostNotFoundException(post_id=post_id)
    return post

def get_posts_by_user(db: Session, skip, limit,  user_id: int) -> list[Post]:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise UserNotFoundException(user_id=user_id)
    return db.query(Post).filter(Post.user_id == user_id).offset(skip).limit(limit).all()

def create_post(db: Session, post: PostCreate, user_id: int) -> Post:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise UserNotFoundException(user_id=user_id)

    db_post = Post(**post.model_dump(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, post_id: int, post: PostUpdate) -> Post:
    db_post = get_post(db, post_id)

    update_data = post.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_post, field, value)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int) -> Post:
    """Delete a post by ID.
    
    Raises:
        PostNotFoundException: If the post does not exist.
    """
    db_post = get_post(db, post_id)  # Reuses existence check + exception
    
    db.delete(db_post)
    db.commit()
    return db_post

