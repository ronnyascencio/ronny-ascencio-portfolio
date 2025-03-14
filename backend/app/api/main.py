from fastapi import FastAPI

from app.api.routers import projects
from app.core.config import frontend_connection

app = FastAPI()
frontend_connection(app)


@app.get("/api/test")
async def test_api():
    return {"message": "¡API funcionando correctamente!", "status": "success"}


app.include_router(projects.router)
