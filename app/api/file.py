# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.files import Files
from api.errors import forbidden
#import json
import datetime
from mongoengine import *

class FilesApi(Resource):
	#@jwt_required
    def get(self) -> Response:

        output = Files.objects()
        return jsonify({'result': output})

class FileApi(Resource):
    
    #@jwt_required
    def get(self, _id) -> Response:
 
        output = Files.objects.get(id=_id)
        return jsonify({'result': output})

class File_nameApi(Resource):
    
    #@jwt_required
    def get(self, filename) -> Response:
 
        output = Files.objects(filename=filename)
        return jsonify({'result': output})
    