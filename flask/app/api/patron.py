# flask packages
from flask import Response, request, jsonify, make_response
from flask import current_app as app
from flask_restful import Resource
#from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.patrons import Patrons
from api.errors import forbidden
import json
from bson.json_util import dumps, loads

from random import sample
#import pandas as pd

import datetime
import calendar
#import Match

from gridfs import GridFS
from mongoengine.fields import get_db



class PatronsApi(Resource):

    #@jwt_required
    def get(self) -> Response:

        output = Patrons.objects()
        return jsonify(output)

class PatronApi(Resource):
    
    #@jwt_required
    def get(self, patron_id) -> Response:
 
        output = Patrons.objects.get(id=patron_id)
        return jsonify(output)

class PatronNameApi(Resource):
    
    #@jwt_required
    def get(self, patron) -> Response:
 
        output = Patrons.objects(patron=patron)
        return jsonify(output)

class PatronDrawApi(Resource):
    
    #@jwt_required
    def get(self) -> Response:

        currentDate = datetime.date.today()
        daysInMonth= calendar.monthrange(currentDate.year, currentDate.month)[1]

        output = Patrons.objects.aggregate([
            {'$sample': { 'size': 1 } },
            #{ '$project': { 'patron': True, 'quotes': { '$slice': [ "$quotes", daysInMonth ] } } }
                                        ])

        json_data = dumps(output, indent = 2)     
        dicts = json.loads(json_data)

        #app.logger.info(dicts[0]['patron'])
        aggregate =  sample(list(dicts[0]['quotes']), k=daysInMonth)
        #app.logger.info(agregate)
        dicts[0]['quotes'] = aggregate

        return dicts[0]['quotes']  

class PatronDownloadImage(Resource):

    #@jwt_required  
    def get(self, filename) -> Response:
        db = get_db()
        gfs = GridFS(db, collection = 'images')
            
        fl = gfs.find_one({"filename": filename})

        response = make_response(fl.read())
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers["Content-Disposition"] = "filename={}".format(filename) +".jpg"

        return response