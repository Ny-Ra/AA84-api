"""
Products domain schemas exports
"""
from .schemas import (
    # Product Category
    ProductCategory, ProductCategoryCreate, ProductCategoryUpdate, 
    ProductCategoryBase, ProductCategoryWithChildren,
    
    # Ingredient
    Ingredient, IngredientCreate, IngredientUpdate, IngredientBase,
    
    # Product
    Product, ProductCreate, ProductUpdate, ProductBase,
    
    # Supplement Category
    SupplementCategory, SupplementCategoryCreate, SupplementCategoryUpdate, SupplementCategoryBase,
    
    # Supplement
    Supplement, SupplementCreate, SupplementUpdate, SupplementBase,
    
    # Supplement-Product Relation
    SupplementProduct, SupplementProductCreate, SupplementProductUpdate, SupplementProductBase,
    
    # Product Availability
    ProductAvailability, ProductAvailabilityCreate, ProductAvailabilityUpdate, ProductAvailabilityBase,
)

__all__ = [
    # Product Category
    "ProductCategory", "ProductCategoryCreate", "ProductCategoryUpdate", 
    "ProductCategoryBase", "ProductCategoryWithChildren",
    
    # Ingredient
    "Ingredient", "IngredientCreate", "IngredientUpdate", "IngredientBase",
    
    # Product
    "Product", "ProductCreate", "ProductUpdate", "ProductBase",
    
    # Supplement Category
    "SupplementCategory", "SupplementCategoryCreate", "SupplementCategoryUpdate", "SupplementCategoryBase",
    
    # Supplement
    "Supplement", "SupplementCreate", "SupplementUpdate", "SupplementBase",
    
    # Supplement-Product Relation
    "SupplementProduct", "SupplementProductCreate", "SupplementProductUpdate", "SupplementProductBase",
    
    # Product Availability
    "ProductAvailability", "ProductAvailabilityCreate", "ProductAvailabilityUpdate", "ProductAvailabilityBase",
]