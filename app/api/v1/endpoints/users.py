from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.user import User, UserCreate

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate,
):
    """
    Admin‑level endpoint to create a user without login.
    """
    if crud.crud_user.get_by_email(db, user_in.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    return crud.crud_user.create(db, user_in)


@router.get("/me", response_model=User)
def read_user_me(current_user: User = Depends(deps.get_current_user)):
    """
    Returns the current authenticated user.
    """
    return current_user
