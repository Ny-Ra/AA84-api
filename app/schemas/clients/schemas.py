"""
Clients domain schemas - All client-related Pydantic models
"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

# =============================================================================
# CLIENT SCHEMAS
# =============================================================================

class ClientBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    phone: str
    marketable: Optional[bool] = None

class ClientCreate(ClientBase):
    password: str
    franchise_id: UUID

class ClientUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    marketable: Optional[bool] = None

class ClientLogin(BaseModel):
    email: EmailStr
    password: str

class Client(ClientBase):
    id: UUID
    created_at: datetime
    franchise_id: UUID

    class Config:
        from_attributes = True

class ClientInDB(Client):
    password: str

# =============================================================================
# ADDRESS SCHEMAS
# =============================================================================

class AddressBase(BaseModel):
    street: str
    phone: str
    entry: str
    door_number: str
    infos: str
    name: str

class AddressCreate(AddressBase):
    client_id: UUID

class AddressUpdate(BaseModel):
    street: Optional[str] = None
    phone: Optional[str] = None
    entry: Optional[str] = None
    door_number: Optional[str] = None
    infos: Optional[str] = None
    name: Optional[str] = None

class Address(AddressBase):
    id: UUID
    client_id: UUID

    class Config:
        from_attributes = True