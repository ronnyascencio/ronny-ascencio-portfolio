from fastapi import APIRouter

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("/")
async def sanity_check_projects():
    return {"message": "¡Projects sanity check!", "status": "success"}
