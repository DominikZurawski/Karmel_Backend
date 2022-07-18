# mongo-engine packages
from mongoengine import *
from datetime import datetime

class Files(Document):
	filename = StringField(max_length=200, required=True)
	#url = StringField()
	chunkSize = IntField()
	length = LongField()
	uploadDate = DateTimeField()

	meta = {
        'collection': 'fs.files'
    }