#!/usr/bin/env bash
# https://gunicorn-docs.readthedocs.io/en/stable/settings.html

from multiprocessing import cpu_count

def max_workers():    
    return cpu_count()
 
#set -o errexit
#set -o pipefail
#set -o nounset
 
#gunicorn config.wsgi:application \
'''
gunicorn app.wsgi:application \
         --bind ${GUNICORN_HOST:-0.0.0.0}:${GUNICORN_PORT:-5000} \
         --timeout ${GUNICORN_TIMEOUT:-300} \
         --workers ${GUNICORN_WORKERS:(2-4) * max_workers()} \
         --threads ${GUNICORN_THREADS:-3 * max_workers()} \
         --worker-class ${GUNICORN_WORKER_CLASS:-sync} \
         --name {{cookiecutter.project_slug}} \
         --access-logfile ${GUNICORN_ACCESS_LOGFILE:-gun.log} \
         --error-logfile ${GUNICORN_ERROR_LOGFILE:--} \
         --chdir /app

'''
#run aplication con gunicorn:
#gunicorn --workers=2 --bind 0.0.0.0:5000  --name KarmelBackend --threads=6 --access-logfile ./gunicorn_access.log --error-logfile ./gunicorn_error.log --daemon --log-level=debug --reload  wsgi:app
