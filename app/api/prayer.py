# flask packages
from flask import Response, request, jsonify, make_response
from flask_restful import Resource

# project resources
from models.prayers import Prayers

from api.errors import forbidden

from gridfs import GridFS
from mongoengine.fields import get_db

from bson import ObjectId

class PrayersApi(Resource):

	#@jwt_required
	def get(self) -> Response:
		output = Prayers.objects()#.first()
		return jsonify(output)
		
class PrayerApi(Resource):
	
	#@jwt_required
	def get(self, prayer_id) -> Response:
		output = Prayers.objects.get(id = prayer_id)
		return jsonify(output)

class PrayerApiDate(Resource):
	
	#@jwt_required
	def get(self, date) -> Response:
		output = Prayers.objects(date = date)
		return jsonify(output)

class PrayerDownloadById(Resource):

	#@jwt_required	
	def get(self, myid) -> Response:
		#output = Prayers.objects(date = date)
		#myid = output[0]['audio']['gospel']['file']
		#name = output[0]['audio']['question1']['filename']

		db = get_db()
		gfs = GridFS(db)
			
		fl = gfs.get(ObjectId(myid))

		response = make_response(fl.read())
		response.headers['Content-Type'] = 'application/octet-stream'
		response.headers["Content-Disposition"] = "filename={}".format(myid) +".mp3"

		return response

class PrayerDownloadByName(Resource):

	#@jwt_required	
	def get(self, filename) -> Response:
		db = get_db()
		gfs = GridFS(db)
			
		fl = gfs.find_one({"filename": filename})

		response = make_response(fl.read())
		response.headers['Content-Type'] = 'application/octet-stream'
		response.headers["Content-Disposition"] = "filename={}".format(filename) +".mp3"

		return response


