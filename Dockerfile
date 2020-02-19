# ---=== USING PYTHON ALPINE BASE ===---#
FROM python:3.7-alpine

# ---=== METADATA ===---#
LABEL Description = "Memory Card BE Python Image"
MAINTAINER Josef Vecernik "josef.vecernik@homecredit.co.in"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# 2DO - Clean this up
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
