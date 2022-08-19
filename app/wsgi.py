from app import get_flask_app

app = get_flask_app()

if __name__ == "__main__":
    app.run()


#run
'''
gunicorn --bind 0.0.0.0:5000 wsgi:app --access-logfile ./gunicorn_access.log --daemon 

--daemon is to keep the process in background.

--access-logfile to keep request log


 gunicorn --workers=5 --bind 0.0.0.0:5000 wsgi:app  --name KarmelBackend --access-logfile ./gunicorn_access.log --daemon

 workers?? default=1
 sudo nano /etc/systemd/system/app.service

 gunicorn --workers=2 --bind 0.0.0.0:5000  --name KarmelBackend --threads=6 --access-logfile ./gunicorn_access.log --error-logfile ./gunicorn_error.log --daemon --log-level=debug --reload  wsgi:app



 '''