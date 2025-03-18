from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session


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

""" variables """
sqlite_filename = "database.db"
sqlite_url = f"sqlite:///./{sqlite_filename}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    with Session(engine) as session:
        yield session
