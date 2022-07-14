# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.images import Images
from api.errors import forbidden
#import json
import datetime
from mongoengine import *

class ImageFilesApi(Resource):
	#@jwt_required
    def get(self) -> Response:

        output = Images.objects()
        return jsonify({'result': output})

class ImageFileApi(Resource):
    
    #@jwt_required
    def get(self, _id) -> Response:
 
        output = Images.objects.get(id=_id)
        return jsonify({'result': output})

class ImageFile_nameApi(Resource):
    
    #@jwt_required
    def get(self, filename) -> Response:
 
        output = Images.objects(filename=filename)
        return jsonify({'result': output})
    