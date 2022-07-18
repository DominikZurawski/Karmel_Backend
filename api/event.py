# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.events import Events
from api.errors import forbidden
#import json

class EventsApi(Resource):

    #@jwt_required
    def get(self) -> Response:

        output = Events.objects()
        #json_data = output.to_json()
        # You might also find it useful to create python dictionaries        
        #dicts = json.loads(json_data)
        #return dicts
        return jsonify(output)

class EventApi(Resource):
    
    #@jwt_required
    def get(self, event_id: str) -> Response:
 
        output = Events.objects.get(id=event_id)
        #json_data = output.to_json()

        # You might also find it useful to create python dictionaries
        
        #dicts = json.loads(json_data)
        #return dicts
        return jsonify(output)
    