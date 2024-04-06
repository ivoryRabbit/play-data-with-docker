import logging
from typing import Dict, Any

from fastapi import APIRouter, HTTPException, Query

from app.config.kafka import producer, TOPIC

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/generate/message")
def send_message(query: str = Query()) -> Dict[str, Any]:
    # TODO: implement kafka producer

    producer.send(topic=TOPIC, value=query)
    producer.flush(1000)
    return {"data": query}
