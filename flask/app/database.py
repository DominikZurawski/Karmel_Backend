import os
from flask_mongoengine import MongoEngine
import pymongo
#from decouple import config
from flask import current_app

def get_host():
    return 'mongodb://' + os.environ['MONGO_INITDB_ROOT_USERNAME'] + ':' + os.environ['MONGO_INITDB_ROOT_PASSWORD'] + \
    '@' + os.environ['MONGODB_HOSTNAME'] + ':' + os.environ['MONGODB_PORT'] + '/' + os.environ['MONGO_INITDB_DATABASE'] + \
    '?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false'
                    
def get_db_instance():
	return os.environ['MONGODB_DATABASE']

def get_database(flask_app):
    db = MongoEngine(app=flask_app)
    return db

def get_db(): # get a connection to the db above
    conn = None
    try:
    	conn = pymongo.MongoClient(get_host())
    except pymongo.errors.ConnectionFailure as e:
       print("Could not connect to MongoDB: %s" % e)
       sys.exit(1)
    return conn
