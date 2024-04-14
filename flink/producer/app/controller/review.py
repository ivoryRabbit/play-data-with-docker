import logging
from typing import Annotated

from fastapi import APIRouter, Depends
from kafka import KafkaProducer
from pydantic import BaseModel, Field

from app.config.kafka import get_kafka_producer, TOPIC

logger = logging.getLogger(__name__)
router = APIRouter()


class Rating(BaseModel):
    user_id: int = Field(..., alias="user_id")
    movie_id: int = Field(..., alias="movie_id")
    rating: float = Field(..., alias="rating")
    timestamp: int = Field(..., alias="timestamp")


@router.post("/rating")
def send_message(rating: Rating, producer: Annotated[KafkaProducer, Depends(get_kafka_producer)]) -> Rating:
    # TODO: implement kafka producer

    payload = rating.model_dump(by_alias=False)
    producer.send(topic=TOPIC, value=payload)
    producer.flush(100)
    return rating
