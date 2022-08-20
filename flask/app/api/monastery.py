# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.monasteries import Monasteries
from api.errors import forbidden
import json


class MonasteriesApi(Resource):

    #@jwt_required
    def get(self) -> Response:

        output = Monasteries.objects()
        #json_data = output.to_json()

        # You might also find it useful to create python dictionaries
        
        #dicts = json.loads(json_data)
        #return dicts
        return jsonify(output)

class MonasteryApi(Resource):
    
    #@jwt_required
    def get(self, monastery_id: str) -> Response:
 
        output = Monasteries.objects.get(id=monastery_id)
        #json_data = output.to_json()

        # You might also find it useful to create python dictionaries
        
        #dicts = json.loads(json_data)
        #return dicts
        return jsonify(output)
    