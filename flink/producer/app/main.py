import logging

from fastapi import FastAPI

from app.config.kafka import init_kafka_producer
from app.config.router import router

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def app_startup() -> None:
    logger.info("App startup")

    # Bootstrap
    init_kafka_producer()

    logger.info("App initiated")


@app.on_event("shutdown")
async def app_shutdown() -> None:
    logger.info("App shutdown")
