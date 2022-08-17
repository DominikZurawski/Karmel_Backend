# flask packages
from flask import Flask, app
from flask_restful import Api
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_jwt_extended import JWTManager
from gridfs import GridFS
from flask_debugtoolbar import DebugToolbarExtension

from database import get_database, get_host
from mongoengine import connect

# local packages
from api.routes import create_routes

# external packages
import os

#run aplication con gunicorn:
#gunicorn --workers=2 --bind 0.0.0.0:5000  --name KarmelBackend --threads=6 --access-logfile ./gunicorn_access.log --error-logfile ./gunicorn_error.log --daemon --log-level=debug --reload  wsgi:app




def get_flask_app(config: dict = None) -> app.Flask:
    """
    Initializes Flask app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    # init flask
    flask_app = Flask(__name__)    
    flask_app.config['JSON_SORT_KEYS'] = False
    #flask_app.config['JSON_AS_ASCII'] = True
    #flask_app.config['JSON_ADD_STATUS'] = True
    #flask_app.config['DEBUG_TB_PANELS'] = ['flask_mongoengine.panels.MongoDebugPanel']
    flask_app.config['JSONIFY_MIMETYPE'] = 'application/json'

    # not working
    #flask_app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    flask_app.debug = True

    # default mongodb configuration
    default_config = {'MONGODB_SETTINGS': {
                    #'db': '*****tg',
                    #'host': 'mongodb',
                    'host': get_host(),
                    #'port': 27017,
                    #'username': 'mongo***',
                    #'password': '******',
                    #'authentication_source': 'admin',
                    #'alias':'default'
                    },
                  #'JWT_SECRET_KEY': 'changeThisKeyFirst'
                  }
    
    # configure app
    config = default_config if config is None else config
    flask_app.config.update(config)
    

    # load config variables
    if 'MONGODB_URI' in os.environ:
        flask_app.config['MONGODB_SETTINGS'] = {'host': os.environ['MONGODB_URI'],
                                                'retryWrites': False}
    #if 'JWT_SECRET_KEY' in os.environ:
    #    flask_app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
    

    # init api and routes
    api = Api(app=flask_app, prefix="/api/v1")
    create_routes(api=api)

    # init mongoengine
    db = get_database(flask_app)
    flask_app.session_interface = MongoEngineSessionInterface(db)
    #fs = GridFS(db)
    flask_app.database = db

    # init jwt manager
    jwt = JWTManager(app=flask_app)

    return flask_app


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    #must be set: iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
    app = get_flask_app()
    
    #dbs = app.db
    #app.debug = True
    app.run(host="0.0.0.0")#,debug=True)



