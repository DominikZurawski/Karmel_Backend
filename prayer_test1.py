import pymongo
from datetime import datetime
import gridfs

myclient = pymongo.MongoClient("mongodb://mongoAdmin:M3hGjZXfQdp53XVL@localhost:27017/Karmel-stg?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
mydb = myclient.test
mydb = myclient['Karmel-stg']
prayer_collection = mydb['prayers']

from mongoengine import *


class AudioFile(Document):
    #id_a = StringField()
    filename = StringField(required=True)
    #file = ReferenceField(fs.files)

    #meta = {'allow_inheritance': True}
    file = FileField()
    

class Audio(Document):
    #audio = StringField()
    #audio = ListField(AudioFile)
    gospel = ListField(AudioFile)
    question1 = ListField(AudioFile)
    question2 = ListField(AudioFile)
    question3 = ListField(AudioFile)
    question4 = ListField(AudioFile)
    

class Gospel(Document):
    #id_g = StringField()
    name = StringField()
    text = StringField()    

class Text(Document):
    #text = StringField()
    gospel = ListField(Gospel)
    contemplation = StringField()
    question = ListField(StringField())

class Bp_data(EmbeddedDocument):   
    date = ListField(DateTimeField())#ComplexDateTimeField(required=True))
    audio = ListField(Audio)
    text = ListField(Text)

class Prayers(Document):
    name = StringField()
    date = EmbeddedDocumentField(Bp_data)

pr = {'name': "elo"}
z = prayer_collection.insert_one(pr)

'''
marmot = Animal(genus='Marmota', family='Sciuridae')

with open('marmot.jpg', 'rb') as fd:
    marmot.photo.put(fd, content_type = 'image/jpeg')
marmot.save()
'''
    

    