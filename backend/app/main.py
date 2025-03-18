from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from sqlmodel import SQLModel

from app.api.main import api_router
from app.core.config import engine, settings


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags}-{route.name}"


SQLModel.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.PROJECT_NAME, generate_unique_id_function=custom_generate_unique_id
)


if settings.all_cors_origins:
    all_cors_origins = settings
else:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/api/health")
async def health_check():
    return {"message": "¡API works!", "status": "success"}


app.include_router(api_router)
