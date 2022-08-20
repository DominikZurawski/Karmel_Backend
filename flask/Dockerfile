# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY ./flask/app flask/app
WORKDIR /flask/app

#COPY requirements.txt /
RUN python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000
