# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY requirements.txt /
RUN python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5000
#CMD [ "python3", "./app/app.py"]

ENTRYPOINT ["./gunicorn.sh"]

#CMD ["/bin/bash"]
#ENTRYPOINT gunicorn --chdir . wsgi:app --workers=2 --bind 0.0.0.0:5000 --name KarmelBackend --threads=6 --access-logfile ./gunicorn_access.log --error-logfile ./gunicorn_error.log --daemon --log-level=debug --reload