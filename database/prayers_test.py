import pymongo
from datetime import datetime
import gridfs
from mongoengine import *
from flask import Response, request, jsonify

import json
from bson import json_util

myclient = pymongo.MongoClient("mongodb://mongoAdmin:M3hGjZXfQdp53XVL@localhost:27017/Karmel-stg?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
mydb = myclient.test
mydb = myclient['Karmel-stg']
prayer_collection = mydb['prayers']
path = '/home/basic-user/nowy/nowy/'
#name = 'Oz_1_wt_41.mp3'
#filedata = open(path+name, 'rb')
#data = filedata.read()
fs = gridfs.GridFS(mydb)#, collection='files')
#fs.put(data, filename=name)
prayer = 	{

    #"prayer" :  {
      #"date": {
      "date": datetime.now(),
              #},                       
      "audio": {
       #"audio":{
          "gospel":{
                "filename": 'Ow02_czw_30_04.mp3',
                "file": fs.put(open(path+'Ow02_czw_30_04.mp3', 'rb'), filename='Ow02_czw_30_04.mp3')
          },
          "question1":{
                "filename": 'Ow02_czw_41_04.mp3',
                "file": fs.put(open(path+'Ow02_czw_41_04.mp3', 'rb'), filename='Ow02_czw_41_04.mp3')
          },
          "question2":{
                "filename": 'Ow02_czw_42_04.mp3',
                "file": fs.put(open(path+'Ow02_czw_42_04.mp3', 'rb'), filename='Ow02_czw_42_04.mp3')
          },
          "question3":{
                "filename": 'Ow02_czw_43_04.mp3',
                "file": fs.put(open(path+'Ow02_czw_43_04.mp3', 'rb'), filename='Ow02_czw_43_04.mp3')
          },
          "question4":{
                "filename": 'Ow02_czw_43_04.mp3',
                "file": fs.put(open(path+'Ow02_czw_43_04.mp3', 'rb'), filename='Ow02_czw_43_04.mp3')
          },

        # },
      },

      "text": {
      #"text": {
          "gospel": {
            "name": 'Ow02_czw_30_04.mp3',
            "text": "Ewangelia według świętego Jana ..."
          },
          "contemplation": "tekst",
          "questions": [
            "Jeden",
          "Dwa"
        ]
      },
      #},
    #}
    }
'''
# mongo-engine packages
from mongoengine import *
from uuid import uuid4
from json import JSONEncoder


class AudioFile(Document):
    filename = StringField(required=True)
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

class Data(EmbeddedDocument):   
    #prayers = StringField()
    date = DateTimeField() #ComplexDateTimeField(required=True))
    audio = ListField(Audio)
    text = ListField(Text)

class Prayers(Document):

    #prayer_id = ObjectIdField(required=True,db_field='_id',primary_key=True)
    #prayer_id = StringField(default=str(uuid4()),db_field='_id')
    #_id = StringField(db_field='_id')
    #_id = ObjectIdField(db_field = '_id')
    #prayer_id = StringField(default=str(uuid4()),primary_key=True)
    prayer = ListField(EmbeddedDocumentField(Data)) #ComplexDateTimeField(required=True))
    #audio = ListField(Audio)
    #text = ListField(Text)


    def default(self, o):
            return o.__dict__


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

odbcArray = []
prayer1 = Prayers()
prayer1.prayer.date = datetime.now()

prayer1.prayer.audio.gospel.filename = 'Ow02_czw_30_04.mp3'
prayer1.prayer.audio.gospel.file = fs.put(open(path+'Ow02_czw_30_04.mp3', 'rb'), filename='Ow02_czw_30_04.mp3')
prayer1.prayer.audio.question1.filename = 'Ow02_czw_41_04.mp3'
prayer1.prayer.audio.question1.file = fs.put(open(path+'Ow02_czw_41_04.mp3', 'rb'), filename='Ow02_czw_41_04.mp3')
prayer1.prayer.audio.question2.filename = 'Ow02_czw_42_04.mp3'
prayer1.prayer.audio.question2.file = fs.put(open(path+'Ow02_czw_42_04.mp3', 'rb'), filename='Ow02_czw_42_04.mp3')
prayer1.prayer.audio.question3.filename = 'Ow02_czw_43_04.mp3'
prayer1.prayer.audio.question3.file = fs.put(open(path+'Ow02_czw_43_04.mp3', 'rb'), filename='Ow02_czw_43_04.mp3')
prayer1.prayer.audio.question4.filename = 'Ow02_czw_43_04.mp3'
prayer1.prayer.audio.question4.file = fs.put(open(path+'Ow02_czw_43_04.mp3', 'rb'), filename='Ow02_czw_43_04.mp3')

prayer1.prayer.text.gospel.name = 'Ow02_czw_30_04.mp3'
prayer1.prayer.text.gospel.text = "Ewangelia według świętego Jana ..."
prayer1.prayer.text.contemplation = "tekst"
prayer1.prayer.text.question = ["Jeden","Dwa"]
'''

z = prayer_collection.insert_one(prayer).inserted_id
#print(prayer1)
#odbcArray.append(prayer1)
#print(prayer1.objects().to_mongo())


#z = prayer_collection.insert_many(json.loads(prayer1.objects().to_json()))

