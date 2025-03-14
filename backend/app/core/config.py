from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def frontend_connection(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:4321"],
        allow_credentials=True,
        allow_methods=["GET"],
        allow_headers=["*"],
    )

    return
