from fastapi import APIRouter, Depends, status, HTTPException
from ..blog_code import models
from ..blog_code.schemas import Login
from ..blog_code.database import get_db
from ..blog_code.hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(tags=["Auth"])


@router.post("/login")
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    return user
