import logging
from typing import Dict, Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.config.kafka import producer, TOPIC

logger = logging.getLogger(__name__)
router = APIRouter()


class Rating(BaseModel):
    user_id: int
    movie_id: int
    rating: float
    timestamp: int


@router.post("/rating")
def send_message(rating: Rating) -> Rating:
    # TODO: implement kafka producer

    producer.send(topic=TOPIC, value=rating.dict())
    producer.flush(100)
    return rating
