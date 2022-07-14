# mongo-engine packages
from mongoengine import *
from datetime import datetime

class Images(Document):	
	width = IntField()
	height = IntField()
	format = StringField()
	thumbnail_id = ObjectIdField()
	filename = StringField(max_length=200, required=True)
	
	#url = StringField()
	chunkSize = IntField()
	length = LongField()
	uploadDate = DateTimeField()

	meta = {
        'collection': 'images.files'
    }