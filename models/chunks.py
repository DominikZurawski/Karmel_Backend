# mongo-engine packages
from mongoengine import *
from datetime import datetime

class Chunks(Document):
  files_id = ObjectIdField(db_field='files_id')
  n = IntField()
  data = BinaryField()

  meta = {
        'collection': 'fs.chunks'
    }