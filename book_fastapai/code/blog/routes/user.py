from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..blog_code.schemas import User, ShowUser
from ..blog_code.models import Base
from ..blog_code.database import engine, SessionLocal, get_db
from ..functions import user

router = APIRouter(
    prefix="/usre",
    tags=["users"],
)


@router.post("/")
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{id}", response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
