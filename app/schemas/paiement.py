from pydantic import BaseModel
from typing import Optional

class PaiementBase(BaseModel):
    name: str

class PaiementCreate(PaiementBase):
    pass

class PaiementUpdate(BaseModel):
    name: Optional[str] = None

class Paiement(PaiementBase):
    id: int

    class Config:
        from_attributes = True