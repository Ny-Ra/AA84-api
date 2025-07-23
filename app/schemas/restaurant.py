from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class RestaurantBase(BaseModel):
    name: str
    pre_order: Optional[bool] = None
    active: bool
    address: str
    postal: str
    state: Optional[str] = None
    city: str

class RestaurantCreate(RestaurantBase):
    franchise_id: UUID

class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    pre_order: Optional[bool] = None
    active: Optional[bool] = None
    address: Optional[str] = None
    postal: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None

class Restaurant(RestaurantBase):
    id: int
    store_id: UUID
    franchise_id: UUID

    class Config:
        from_attributes = True