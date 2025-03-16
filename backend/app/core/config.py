from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    def all_cors_origins(app: str):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:4321"],
            allow_credentials=True,
            allow_methods=["GET"],
            allow_headers=["*"],
        )

        return

    PROJECT_NAME: str = "Website Ronny Ascencio"


settings = Settings()
