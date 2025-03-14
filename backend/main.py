from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS para permitir peticiones desde tu frontend en Astro
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4321"
    ],  # Puedes especificar el dominio exacto si deseas mayor seguridad
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api/test")
async def test_api():
    return {"message": "¡API funcionando correctamente!", "status": "success"}
