from fastapi import APIRouter

from api.api_v1.routers import router as router_api_v1
from core.config import settings


router = APIRouter(prefix=settings.api.prefix)
router.include_router(router_api_v1)
