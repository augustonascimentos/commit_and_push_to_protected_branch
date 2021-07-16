FROM python:3-alpine AS builder

ADD . /app
WORKDIR /app

RUN pip install --target=/app requests

COPY --from=builder /app /app

RUN apk update \
    && apk add --no-cache git bash

WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]
