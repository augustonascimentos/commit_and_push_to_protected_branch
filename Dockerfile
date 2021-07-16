FROM python:3-alpine AS builder

ADD . /app
WORKDIR /app

RUN pip install --target=/app requests
RUN apk update \
    && apk add --no-cache git bash

WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]
