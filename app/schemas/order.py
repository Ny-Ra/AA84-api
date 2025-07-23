from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

class OrderBase(BaseModel):
    order_number: str
    status: Optional[str] = None
    total_price: float
    discount_type: Optional[str] = None
    discount_order: Optional[float] = None
    comment: Optional[str] = None

class OrderCreate(OrderBase):
    order_type_id: int
    client_id: int
    restaurant_id: int
    paiement_id: Optional[int] = None

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    total_price: Optional[float] = None
    discount_type: Optional[str] = None
    discount_order: Optional[float] = None
    comment: Optional[str] = None
    paiement_id: Optional[int] = None

class Order(OrderBase):
    id: int
    created_at: datetime
    order_type_id: int
    client_id: int
    restaurant_id: int
    paiement_id: Optional[int] = None

    class Config:
        from_attributes = True

class OrderWithItems(Order):
    items: List["OrderItem"] = []