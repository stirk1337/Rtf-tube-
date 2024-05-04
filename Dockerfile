FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./

RUN apt update && \
    apt install ffmpeg libpq-dev gcc -y &&  \
    pip install -r /app/requirements.txt

COPY . .