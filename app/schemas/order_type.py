from pydantic import BaseModel
from typing import Optional

class OrderTypeBase(BaseModel):
    type: str

class OrderTypeCreate(OrderTypeBase):
    pass

class OrderTypeUpdate(BaseModel):
    type: Optional[str] = None

class OrderType(OrderTypeBase):
    id: int

    class Config:
        from_attributes = True