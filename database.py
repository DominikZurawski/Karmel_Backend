from flask_mongoengine import MongoEngine
import pymongo
from decouple import config
from flask import current_app

def get_db_instance():
	return 'Karmel-stg'

def get_database(flask_app):
    db = MongoEngine(app=flask_app)
    return db

def get_db(): # get a connection to the db above
    conn = None
    try:
    	conn = pymongo.MongoClient(config('DATABASE_URL'))
    except pymongo.errors.ConnectionFailure as e:
       print("Could not connect to MongoDB: %s" % e)
       sys.exit(1)
    return conn



