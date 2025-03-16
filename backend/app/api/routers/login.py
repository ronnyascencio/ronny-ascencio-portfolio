from fastapi import APIRouter

router = APIRouter(prefix="/login", tags=["Login"])


@router.get("/")
async def sanity_check_login():
    return {"message": "¡Login sanity check!", "status": "success"}
