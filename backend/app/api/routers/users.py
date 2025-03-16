from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def sanity_check_projects():
    return {"message": "¡Users sanity check!", "status": "success"}
