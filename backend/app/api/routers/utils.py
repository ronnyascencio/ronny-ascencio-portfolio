from fastapi import APIRouter

router = APIRouter(prefix="/utils", tags=["Utils"])


@router.get("/")
async def sanity_check_utils():
    return {"message": "¡utils sanity check!", "status": "success"}
