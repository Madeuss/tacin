from fastapi import APIRouter
from my_api.api.v1 import items

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
