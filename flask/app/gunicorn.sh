#!/bin/sh
#gunicorn --chdir /app wsgi:app --workers=2 --bind 0.0.0.0:5030 --name KarmelBackend --threads=6 --access-logfile ./gunicorn_access.log --error-logfile ./gunicorn_error.log --daemon --log-level=debug --reload --reload
gunicorn --chdir /app wsgi:app -w 2 --threads 6 -b 0.0.0.0:5030  --access-logfile ./gunicorn_access.log --error-logfile ./gunicorn_error.log --name KarmelBackend --log-level=debug --reload
# --daemon
# -D