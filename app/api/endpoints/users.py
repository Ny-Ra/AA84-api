from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user import User, UserCreate

router = APIRouter()

@router.get("/", response_model=List[User])
async def read_users():
    return [{"id": 1, "name": "John Doe", "email": "john@example.com"}]

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    if user_id == 1:
        return {"id": 1, "name": "John Doe", "email": "john@example.com"}
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    return {"id": 2, "name": user.name, "email": user.email}