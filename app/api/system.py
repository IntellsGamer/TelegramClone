from fastapi import APIRouter, Depends, Request

from app.api.deps import get_env_detector, get_feature_manager
from app.core.feature_manager import FeatureManager
from app.services.environment import EnvironmentDetector

router = APIRouter(prefix="/api", tags=["system"])


@router.get("/health")
async def healthcheck(request: Request, env_detector: EnvironmentDetector = Depends(get_env_detector)):
    protocol_info = env_detector.detect(request)
    return {
        "status": "ok",
        "protocol": protocol_info.protocol,
        "websocket_protocol": protocol_info.websocket_protocol,
        "via_proxy": protocol_info.via_proxy,
    }


@router.get("/admin/features")
async def feature_matrix(features: FeatureManager = Depends(get_feature_manager)):
    return {item.name: item.enabled for item in features.matrix()}
