from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.orm import Session
from typing import List
import bcrypt
import jwt
import os
from generate_password import generate
from app.core.database import get_db
from app.models.users import User
from app.schemas.users.schemas import (
    User as UserSchema, 
    UserCreate, 
    UserLogin,
    UserInDB
)

router = APIRouter()

@router.post("/login")
async def login_user(login_data: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.email).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Le compte saisi n'existe pas !")
    
    # Verify password
    if not bcrypt.checkpw(login_data.password.encode('utf-8'), user.password.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Le mot de passe est incorrect")
    
    # Generate JWT token
    secret_token = os.getenv("SECRET_TOKEN", "default-secret-key")
    token = jwt.encode({"id": str(user.id)}, secret_token, algorithm="HS256")
    
    # Set token in header
    response.headers["token"] = token
    
    return {"token": token, "user": user}

@router.post("/", response_model=UserSchema)
async def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(
        User.email == user_data.email,
        User.franchise_id == user_data.franchise_id
    ).first()
    
    if existing_user:
        raise HTTPException(status_code=401, detail="Le compte existe déjà !")
    
    # Hash password
    salt = bcrypt.gensalt(rounds=15)
    hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), salt)
    
    try:
        # Create new user
        db_user = User(
            firstname=user_data.firstname,
            lastname=user_data.lastname,
            email=user_data.email,
            password=hashed_password.decode('utf-8'),
            franchise_id=user_data.franchise_id
        )
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=404, detail="Une erreur est survenu")

@router.post("/reset-password")
async def reset_password(email_data: dict, db: Session = Depends(get_db)):
    email = email_data.get("email")
    
    # Find existing user
    existing_user = db.query(User).filter(User.email == email).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="Le compte saisi n'existe pas !")
    
    # Generate new password
    new_password = generate(length=15, numbers=True)
    salt = bcrypt.gensalt(rounds=15)
    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), salt)
    
    try:
        # Update password in database
        existing_user.password = hashed_password.decode('utf-8')
        db.commit()

        return {
            "message": "Mot de passe réinitialisé avec succès",
            "new_password": new_password
        }
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Une erreur est survenue: {str(e)}")

@router.get("/", response_model=List[UserSchema])
async def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{user_id}", response_model=UserSchema)
async def read_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user