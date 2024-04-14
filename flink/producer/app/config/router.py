from fastapi import APIRouter

from app.controller import ping, review

router = APIRouter()

router.include_router(router=ping.router, prefix="", tags=["ping"])
router.include_router(router=review.router, prefix="/review", tags=["review"])
