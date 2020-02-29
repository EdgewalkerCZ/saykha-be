# ---=== USING PYTHON ALPINE BASE ===---#
FROM python:3.7-alpine

# ---=== METADATA ===---#
LABEL Description = "Memory Card BE Python Image"
MAINTAINER Josef Vecernik "josef.vecernik@homecredit.co.in"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# 2DO - Clean this up
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
