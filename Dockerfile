FROM python:alpine

COPY requirements*.txt ./
COPY src ./src

RUN apk update \
    && apk add --no-cache git bash \
    && pip install -r requirements.txt
RUN chmod +x src/main.py

CMD ["src/main.py"]
ENTRYPOINT [ "python3" ]
