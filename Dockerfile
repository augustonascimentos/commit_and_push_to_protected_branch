FROM python:3-slim AS builder

ADD . /app
WORKDIR /app

RUN pip install --target=/app requests

FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app

RUN apk update \
    && apk add --no-cache git bash

WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]
