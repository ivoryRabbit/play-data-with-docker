FROM python:3.9-slim

WORKDIR /opt/server/

COPY ./producer/requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ./producer/app ./app
