import logging

from fastapi import FastAPI

from app.bootstrap.dataset import load_data
from app.config.router import router

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def app_startup() -> None:
    logger.info("App startup")

    # Bootstrap
    load_data(path="/tmp/flink/dataset")

    logger.info("App initiated")


@app.on_event("shutdown")
async def app_shutdown() -> None:
    logger.info("App shutdown")
