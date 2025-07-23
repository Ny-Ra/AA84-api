"""
Orders domain schemas - All order-related Pydantic models
"""
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from datetime import datetime
from decimal import Decimal

# =============================================================================
# PAYMENT METHOD SCHEMAS
# =============================================================================

class PaiementBase(BaseModel):
    name: str

class PaiementCreate(PaiementBase):
    pass

class PaiementUpdate(BaseModel):
    name: Optional[str] = None

class Paiement(PaiementBase):
    id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# ORDER TYPE SCHEMAS
# =============================================================================

class OrderTypeBase(BaseModel):
    type: str

class OrderTypeCreate(OrderTypeBase):
    pass

class OrderTypeUpdate(BaseModel):
    type: Optional[str] = None

class OrderType(OrderTypeBase):
    id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# ORDER SCHEMAS
# =============================================================================

class OrderBase(BaseModel):
    order_number: str
    status: Optional[str] = None
    total_price: float
    discount_type: Optional[str] = None
    discount_order: Optional[float] = None
    comment: Optional[str] = None

class OrderCreate(OrderBase):
    order_type_id: UUID
    client_id: UUID
    restaurant_id: UUID
    paiement_id: Optional[UUID] = None

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    total_price: Optional[float] = None
    discount_type: Optional[str] = None
    discount_order: Optional[float] = None
    comment: Optional[str] = None
    paiement_id: Optional[UUID] = None

class Order(OrderBase):
    id: UUID
    created_at: datetime
    order_type_id: UUID
    client_id: UUID
    restaurant_id: UUID
    paiement_id: Optional[UUID] = None

    class Config:
        from_attributes = True

class OrderWithItems(Order):
    items: List["OrderItem"] = []

# =============================================================================
# ORDER ITEM SCHEMAS
# =============================================================================

class OrderItemBase(BaseModel):
    price: Decimal
    quantity: str
    comment: Optional[str] = None
    discount_type: Optional[str] = None
    discount_price: Optional[Decimal] = None

class OrderItemCreate(OrderItemBase):
    product_id: UUID
    order_id: UUID

class OrderItemUpdate(BaseModel):
    price: Optional[Decimal] = None
    quantity: Optional[str] = None
    comment: Optional[str] = None
    discount_type: Optional[str] = None
    discount_price: Optional[Decimal] = None

class OrderItem(OrderItemBase):
    id: UUID
    product_id: UUID
    order_id: UUID

    class Config:
        from_attributes = True

class OrderItemWithExtras(OrderItem):
    extras: List["OrderItemExtra"] = []

# =============================================================================
# ORDER ITEM EXTRA SCHEMAS
# =============================================================================

class OrderItemExtraBase(BaseModel):
    price: Decimal
    quantity: str

class OrderItemExtraCreate(OrderItemExtraBase):
    order_item_id: UUID
    supplement_id: UUID

class OrderItemExtraUpdate(BaseModel):
    price: Optional[Decimal] = None
    quantity: Optional[str] = None

class OrderItemExtra(OrderItemExtraBase):
    id: UUID
    order_item_id: UUID
    supplement_id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# ORDER STATUS HISTORY SCHEMAS
# =============================================================================

class OrderStatusHistoryBase(BaseModel):
    status: str
    notes: Optional[str] = None

class OrderStatusHistoryCreate(OrderStatusHistoryBase):
    order_id: UUID
    changed_by_user_id: Optional[UUID] = None

class OrderStatusHistoryUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None

class OrderStatusHistory(OrderStatusHistoryBase):
    id: UUID
    timestamp: datetime
    order_id: UUID
    changed_by_user_id: Optional[UUID] = None

    class Config:
        from_attributes = True