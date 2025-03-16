from fastapi import APIRouter

from app.api.routers import login, projects, users, utils

api_router = APIRouter()
api_router.include_router(projects.router)
api_router.include_router(utils.router)
api_router.include_router(users.router)
api_router.include_router(login.router)
