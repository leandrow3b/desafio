FROM python:3.7.8-alpine

EXPOSE 8080

ENV PYTHONBUFFERED 1

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

RUN apk del build-deps

ADD . /code

CMD ["python3", "main.py"]
