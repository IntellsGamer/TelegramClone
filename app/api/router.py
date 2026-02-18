from fastapi import APIRouter

from app.api.auth import router as auth_router
from app.api.chats import router as chats_router
from app.api.system import router as system_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(chats_router)
api_router.include_router(system_router)
