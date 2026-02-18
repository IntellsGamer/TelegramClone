from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db, get_feature_manager
from app.core.feature_manager import FeatureManager
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.services.auth import login_user, register_user

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register")
async def register(
    payload: RegisterRequest,
    db: AsyncSession = Depends(get_db),
    features: FeatureManager = Depends(get_feature_manager),
):
    return await register_user(db, payload, features)


@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    token = await login_user(db, payload)
    return TokenResponse(access_token=token)


@router.post("/verify-email")
async def verify_email(features: FeatureManager = Depends(get_feature_manager)):
    if not features.enabled("email_verification"):
        return {"enabled": False, "detail": "Email verification disabled"}
    return {"enabled": True, "detail": "Verification endpoint available"}
