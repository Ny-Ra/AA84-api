"""
Restaurants domain schemas - All restaurant-related Pydantic models
"""
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from decimal import Decimal

# =============================================================================
# RESTAURANT SCHEMAS
# =============================================================================

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
    id: UUID
    store_id: UUID
    franchise_id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# OPERATING HOURS SCHEMAS
# =============================================================================

class HourBase(BaseModel):
    start: str
    end: str
    day: str
    active: bool = True
    shift: Optional[str] = None

class HourCreate(HourBase):
    restaurant_id: UUID

class HourUpdate(BaseModel):
    start: Optional[str] = None
    end: Optional[str] = None
    day: Optional[str] = None
    active: Optional[bool] = None
    shift: Optional[str] = None

class Hour(HourBase):
    id: UUID
    restaurant_id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# DELIVERY ZONE SCHEMAS
# =============================================================================

class DeliveryZoneBase(BaseModel):
    zone_number: str
    color: str
    disabled: bool
    min_order: Decimal
    d_fee: Decimal

class DeliveryZoneCreate(DeliveryZoneBase):
    restaurant_id: UUID

class DeliveryZoneUpdate(BaseModel):
    zone_number: Optional[str] = None
    color: Optional[str] = None
    disabled: Optional[bool] = None
    min_order: Optional[Decimal] = None
    d_fee: Optional[Decimal] = None

class DeliveryZone(DeliveryZoneBase):
    id: UUID
    restaurant_id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# DELIVERY POINT SCHEMAS
# =============================================================================

class DeliveryPointBase(BaseModel):
    lat: float
    lng: float

class DeliveryPointCreate(DeliveryPointBase):
    zone_id: UUID

class DeliveryPointUpdate(BaseModel):
    lat: Optional[float] = None
    lng: Optional[float] = None

class DeliveryPoint(DeliveryPointBase):
    id: UUID
    zone_id: UUID

    class Config:
        from_attributes = True