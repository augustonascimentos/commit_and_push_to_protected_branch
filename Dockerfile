FROM python:alpine

ADD requirements*.txt ./
ADD src ./src

RUN apk update \
    && apk add --no-cache git bash \
    && pip install -r requirements.txt

CMD ["./src/main.py"]
ENTRYPOINT [ "python3" ]
