from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.core.config import get_session
from app.models import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def sanity_check_projects():
    return {"message": "¡Users sanity check!", "status": "success"}


"""CRUD Users"""

session = get_session()


@router.post("/create", response_model=User)
async def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.get("/read/", response_model=list[User])
async def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.excec(select(User)).offset(skip).limit(limit).all()
    return users
