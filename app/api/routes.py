from fastapi import APIRouter
from app.api.endpoints import users, franchises

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(franchises.router, prefix="/franchises", tags=["franchises"])