# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY ./app /app
WORKDIR /app

#COPY requirements.txt /
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt #--no-cache-dir

EXPOSE 5000

CMD exec gunicorn --chdir /flask/app wsgi:app -w 2 --threads 6 -b 0.0.0.0:5000  --access-logfile ./gunicorn_access.log --error-logfile ./gunicorn_error.log --name KarmelBackend --log-level=debug --reload