from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck")
async def healtcheck():
    return {"status": "OK"}
