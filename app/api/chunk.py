# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.chunks import Chunks
from api.errors import forbidden
#import json
import datetime
from mongoengine import *
'''
class ChunksApi(Resource):
	#@jwt_required
    def get(self) -> Response:

        output = Chunks.objects()
        return jsonify({'result': output})
'''
class ChunkApi(Resource):
    
    #@jwt_required
    def get(self, _id) -> Response:
 
        output = Chunks.objects.get(id=_id)
        return jsonify({'result': output})

class Chunk_idApi(Resource):
    
    #@jwt_required
    def get(self, files_id) -> Response:
 
        output = Chunks.objects(files_id=files_id)
        return jsonify({'result': output})
    