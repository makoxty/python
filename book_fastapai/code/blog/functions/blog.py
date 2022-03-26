from hashlib import new
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..blog_code import models
from ..blog_code.schemas import Blog


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(blog: Blog, db: Session):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    blog.delete(synchronize_session=False)
    db.commit()


def update(id: int, request: Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    blog.update({"title": request.title, "body": request.body})
    db.commit()
    return "Updated"
