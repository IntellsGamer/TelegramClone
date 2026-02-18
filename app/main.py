from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.router import api_router
from app.core.feature_manager import FeatureManager
from app.core.settings import get_settings
from app.services.environment import EnvironmentDetector
from app.templates.views import router as template_router
from app.ws.stream import router as ws_router


def create_app() -> FastAPI:
    settings = get_settings()
    feature_manager = FeatureManager(settings=settings)
    env_detector = EnvironmentDetector(settings=settings)

    app = FastAPI(title=settings.app_name)
    app.state.settings = settings
    app.state.feature_manager = feature_manager
    app.state.env_detector = env_detector

    app.include_router(api_router)
    app.include_router(ws_router)
    app.include_router(template_router)
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    return app


app = create_app()
