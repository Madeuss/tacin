from fastapi import APIRouter
from my_api.schemas.item import Item, ItemCreate

router = APIRouter()

@router.post("/", response_model=Item)
def create_item(item: ItemCreate):
    return Item(id=1, name=item.name, description=item.description)
