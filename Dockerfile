FROM python:alpine

COPY requirements*.txt ./
COPY src .

RUN apk update \
    && apk add --no-cache git bash \
    && pip install -r requirements.txt
RUN chmod +x main.py

CMD ["main.py"]
ENTRYPOINT [ "python3" ]
