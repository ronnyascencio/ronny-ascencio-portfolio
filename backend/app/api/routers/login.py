from typing import Annotated

from fastapi import APIRouter, Form

router = APIRouter(prefix="/login", tags=["Login"])


@router.get("/")
async def sanity_check_login():
    return {"message": "¡Login sanity check!", "status": "success"}


@router.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
