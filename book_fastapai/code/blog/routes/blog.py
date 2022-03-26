from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..functions import blog
from ..blog_code.database import get_db
from ..blog_code.schemas import ShowBlog, Blog
from ..blog_code import models

router = APIRouter(
    prefix="/blog",
    tags=["blogs"],
)


@router.get("/", response_model=List[ShowBlog])
def all_fetch(db: Session = Depends(get_db)):
    blogs = blog.get_all(db)
    return blogs


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowBlog,
)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    return blog


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
def update(id, request: Blog, db: Session = Depends(get_db)):
    return blog.update(id, db)
