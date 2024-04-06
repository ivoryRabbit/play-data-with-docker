from fastapi import APIRouter

from app.router import ping, generate

router = APIRouter()

router.include_router(router=ping.router, prefix="", tags=["ping"])
router.include_router(router=generate.router, prefix="/generate", tags=["generate"])
