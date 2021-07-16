FROM python:alpine

COPY requirements*.txt ./
COPY src ./src

RUN echo $GITHUB_REPOSITORY

RUN apk update \
    && apk add --no-cache git bash \
    && pip install -r requirements.txt
RUN chmod +x src/main.py

ENTRYPOINT [ "src/main.py" ]
