from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

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
    id: int
    created_at: datetime
    franchise_id: UUID

    class Config:
        from_attributes = True

class ClientInDB(Client):
    password: str