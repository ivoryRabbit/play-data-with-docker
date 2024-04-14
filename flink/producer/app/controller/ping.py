import logging

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
@router.get("/ping")
@router.get("/health")
def health_check(request: Request) -> JSONResponse:
    # if hasattr(request.app.state, "producer") is False:
    #     logger.error("Kafka Producer is not prepared yet")
    #     raise HTTPException(status_code=400)

    return JSONResponse(content={"ok": "ok"})
