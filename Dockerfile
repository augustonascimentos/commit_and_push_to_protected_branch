FROM ubuntu:latest
# FROM python:3-slim AS builder
ADD . /app
WORKDIR /app


# FROM gcr.io/distroless/python3-debian10

RUN apt update && apt install -y git
RUN apt install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa
RUN apt update && apt install python3.8
RUN pip install --target=/app requests

# COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]
