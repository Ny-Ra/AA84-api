from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class FranchiseBase(BaseModel):
    name: str

class FranchiseCreate(FranchiseBase):
    pass

class FranchiseUpdate(BaseModel):
    name: Optional[str] = None

class Franchise(FranchiseBase):
    corporation_id: UUID

    class Config:
        from_attributes = True