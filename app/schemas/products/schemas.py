"""
Products domain schemas - All product-related Pydantic models
"""
from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional, List
from uuid import UUID
from decimal import Decimal

# =============================================================================
# PRODUCT CATEGORY SCHEMAS
# =============================================================================

class ProductCategoryBase(BaseModel):
    name: str

class ProductCategoryCreate(ProductCategoryBase):
    franchise_id: UUID
    parent_category_id: Optional[UUID] = None

class ProductCategoryUpdate(BaseModel):
    name: Optional[str] = None
    parent_category_id: Optional[UUID] = None

class ProductCategory(ProductCategoryBase):
    id: UUID
    franchise_id: UUID
    parent_category_id: Optional[UUID] = None

    class Config:
        from_attributes = True

class ProductCategoryWithChildren(ProductCategory):
    child_categories: List["ProductCategory"] = []

# =============================================================================
# INGREDIENT SCHEMAS
# =============================================================================

class IngredientBase(BaseModel):
    name: str

class IngredientCreate(IngredientBase):
    franchise_id: UUID

class IngredientUpdate(BaseModel):
    name: Optional[str] = None

class Ingredient(IngredientBase):
    id: UUID
    franchise_id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# PRODUCT SCHEMAS
# =============================================================================

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    price: Decimal = Field(..., gt=0, decimal_places=2)
    vat: Optional[str] = Field(None, max_length=10)
    image: Optional[str] = Field(None, max_length=500)
    description: Optional[str] = Field(None, max_length=1000)
    additionnal_sale: Optional[bool] = False

    @validator('name')
    def validate_name(cls, v):
        if not v or not v.strip():
            raise ValueError('Product name cannot be empty')
        return v.strip()

class ProductCreate(ProductBase):
    category_id: UUID
    franchise_id: UUID

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[Decimal] = None
    vat: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    additionnal_sale: Optional[bool] = None
    category_id: Optional[UUID] = None

class Product(ProductBase):
    id: UUID
    category_id: UUID
    franchise_id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# SUPPLEMENT CATEGORY SCHEMAS
# =============================================================================

class SupplementCategoryBase(BaseModel):
    name: str

class SupplementCategoryCreate(SupplementCategoryBase):
    franchise_id: UUID

class SupplementCategoryUpdate(BaseModel):
    name: Optional[str] = None

class SupplementCategory(SupplementCategoryBase):
    id: UUID
    franchise_id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# SUPPLEMENT SCHEMAS
# =============================================================================

class SupplementBase(BaseModel):
    name: str
    price: Decimal
    image: Optional[str] = None

class SupplementCreate(SupplementBase):
    category_id: UUID

class SupplementUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[Decimal] = None
    image: Optional[str] = None
    category_id: Optional[UUID] = None

class Supplement(SupplementBase):
    id: UUID
    category_id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# SUPPLEMENT-PRODUCT RELATION SCHEMAS
# =============================================================================

class SupplementProductBase(BaseModel):
    number_free: Optional[str] = None
    min: Optional[str] = None
    max: Optional[str] = None

class SupplementProductCreate(SupplementProductBase):
    product_id: UUID
    category_id: UUID

class SupplementProductUpdate(BaseModel):
    number_free: Optional[str] = None
    min: Optional[str] = None
    max: Optional[str] = None

class SupplementProduct(SupplementProductBase):
    id: UUID
    product_id: UUID
    category_id: UUID

    class Config:
        from_attributes = True

# =============================================================================
# PRODUCT AVAILABILITY SCHEMAS
# =============================================================================

class ProductAvailabilityBase(BaseModel):
    availability: bool = True

class ProductAvailabilityCreate(ProductAvailabilityBase):
    product_id: UUID
    restaurant_id: UUID

class ProductAvailabilityUpdate(BaseModel):
    availability: Optional[bool] = None

class ProductAvailability(ProductAvailabilityBase):
    id: UUID
    product_id: UUID
    restaurant_id: UUID

    class Config:
        from_attributes = True