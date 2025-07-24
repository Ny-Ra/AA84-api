from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.franchise import Franchise
from app.schemas.core.franchise import FranchiseCreate, Franchise as FranchiseSchema

router = APIRouter()

@router.post("/", response_model=FranchiseSchema)
async def add_franchise(franchise: FranchiseCreate, db: Session = Depends(get_db)):
    try:
        db_franchise = Franchise(name=franchise.name)
        db.add(db_franchise)
        db.commit()
        db.refresh(db_franchise)
        return db_franchise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[FranchiseSchema])
async def get_franchises(db: Session = Depends(get_db)):
    return db.query(Franchise).all()

@router.get("/{franchise_id}", response_model=FranchiseSchema)
async def get_franchise(franchise_id: str, db: Session = Depends(get_db)):
    franchise = db.query(Franchise).filter(Franchise.id == franchise_id).first()
    if not franchise:
        raise HTTPException(status_code=404, detail="Franchise not found")
    return franchise