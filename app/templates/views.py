from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.core.feature_manager import FeatureManager

router = APIRouter(tags=["web"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def telegram_clone_ui(request: Request):
    feature_manager: FeatureManager = request.app.state.feature_manager
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "theme": "dark",
            "features": {item.name: item.enabled for item in feature_manager.matrix()},
        },
    )
