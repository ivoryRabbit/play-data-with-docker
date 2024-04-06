import json

# from fastapi import FastAPI
from kafka import KafkaProducer


BOOTSTRAP_SERVERS = ["localhost:9094"]
TOPIC = "input.flink.dev"

# def register_kafka_config(app: FastAPI) -> None:
#     await scheduler.build_graph(app)


producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)