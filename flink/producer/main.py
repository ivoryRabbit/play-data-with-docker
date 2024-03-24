from operator import itemgetter

from fastapi import FastAPI
from kafka import KafkaProducer


app = FastAPI()


@app.get("/reactor/send_message")
def send_message(query: str):
    # TODO: implement kafka producer
    return {"data": query}
