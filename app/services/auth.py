from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.feature_manager import FeatureManager
from app.models.entities import User
from app.schemas.auth import LoginRequest, RegisterRequest
from app.services.security import create_access_token, hash_password, verify_password


async def register_user(db: AsyncSession, payload: RegisterRequest, features: FeatureManager) -> dict:
    if payload.email and not features.enabled("email_verification"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email registration is disabled")

    existing = await db.scalar(select(User).where(User.username == payload.username))
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")

    user = User(username=payload.username, email=payload.email, password_hash=hash_password(payload.password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return {"id": user.id, "username": user.username}


async def login_user(db: AsyncSession, payload: LoginRequest) -> str:
    user = await db.scalar(select(User).where(User.username == payload.username))
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return create_access_token(subject=str(user.id))
