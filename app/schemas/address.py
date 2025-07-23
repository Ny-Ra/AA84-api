from pydantic import BaseModel
from typing import Optional

class AddressBase(BaseModel):
    street: str
    phone: str
    entry: str
    door_number: str
    infos: str
    name: str

class AddressCreate(AddressBase):
    client_id: int

class AddressUpdate(BaseModel):
    street: Optional[str] = None
    phone: Optional[str] = None
    entry: Optional[str] = None
    door_number: Optional[str] = None
    infos: Optional[str] = None
    name: Optional[str] = None

class Address(AddressBase):
    id: int
    client_id: int

    class Config:
        from_attributes = True