import json
from functools import lru_cache
from typing import Optional

from kafka import KafkaProducer


BOOTSTRAP_SERVERS = ["kafka:9092"]
TOPIC = "input.flink.dev"

_producer: Optional[KafkaProducer] = None


@lru_cache
def get_kafka_producer() -> KafkaProducer:
    global _producer
    assert _producer is not None
    return _producer


def init_kafka_producer() -> None:
    global _producer

    _producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda x: json.dumps(x).encode("utf-8")
    )
