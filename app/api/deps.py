from fastapi import Depends, Request

from app.core.feature_manager import FeatureManager
from app.db.session import get_db


def get_feature_manager(request: Request) -> FeatureManager:
    return request.app.state.feature_manager


def get_env_detector(request: Request):
    return request.app.state.env_detector


__all__ = ["Depends", "get_db", "get_feature_manager", "get_env_detector"]
