from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.item import Item, ItemCreate

router = APIRouter()

@router.get("/", response_model=List[Item])
async def read_items():
    return [{"id": 1, "title": "Sample Item", "description": "This is a sample item"}]

@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id == 1:
        return {"id": 1, "title": "Sample Item", "description": "This is a sample item"}
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("/", response_model=Item)
async def create_item(item: ItemCreate):
    return {"id": 2, "title": item.title, "description": item.description}