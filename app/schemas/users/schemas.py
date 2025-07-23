"""
Users domain schemas - All user-related Pydantic models
"""
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from uuid import UUID

# =============================================================================
# USER SCHEMAS
# =============================================================================

class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    franchise_id: UUID

class UserUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: UUID
    franchise_id: UUID

    class Config:
        from_attributes = True

class UserInDB(User):
    password: str

# =============================================================================
# PERMISSION SCHEMAS
# =============================================================================

class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None
    resource: str
    action: str

class PermissionCreate(PermissionBase):
    pass

class PermissionUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    resource: Optional[str] = None
    action: Optional[str] = None

class Permission(PermissionBase):
    id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# ROLE SCHEMAS
# =============================================================================

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_system: bool = False

class RoleCreate(RoleBase):
    franchise_id: Optional[UUID] = None

class RoleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class Role(RoleBase):
    id: UUID
    franchise_id: Optional[UUID] = None

    class Config:
        from_attributes = True

class RoleWithPermissions(Role):
    permissions: List[Permission] = []

# =============================================================================
# USER SESSION SCHEMAS
# =============================================================================

class UserSessionBase(BaseModel):
    session_token: str
    created_at: str
    expires_at: str
    is_active: bool = True
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None

class UserSessionCreate(UserSessionBase):
    user_id: UUID

class UserSessionUpdate(BaseModel):
    is_active: Optional[bool] = None
    expires_at: Optional[str] = None

class UserSession(UserSessionBase):
    id: UUID
    user_id: UUID

    class Config:
        from_attributes = True