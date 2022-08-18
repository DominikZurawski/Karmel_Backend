from datetime import datetime
#import gridfs
#from mongoengine import *
import pymongo
from PIL import Image

from mongoengine import *
from karmel_backend.app.models.monasteries import Monasteries

connect = connect(host="mongodb://mongoAdmin:M3hGjZXfQdp53XVL@localhost:27017/Karmel-stg?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")

class Events(Document):
    id_event = IntField(unique = True)
    title = StringField(max_length=240)    
    description = StringField()
    event_type = DictField()
    start_date = DateTimeField()
    end_date = DateTimeField()    
    link = StringField()
    location = ReferenceField(Monasteries)


_id = 1010
events = 2
titles = "KDM"

E = Events(id_event = events)
E.title = titles
E.description = "Karmelitańskie Dni Młodzieży"
E.save()

i = Events.objects(id_event = events).get()
i.start_date = datetime(2023,7,28)
i.save()

j = Events.objects(id_event = events).get()
j.end_date = datetime(2023,7,31)
j.save()

o = Events.objects(id_event = events).get()
o.link = "url"
o.event_type = {
              "id_type": "OCDS",
              "name": "Świecki Zakon",
              "color_code": "green"
              }
o.location = Monasteries.objects(id_monastery= _id).get()

o.save()

'''
myclient = pymongo.MongoClient("mongodb://mongoAdmin:M3hGjZXfQdp53XVL@localhost:27017/Karmel-stg?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
mydb = myclient.test
mydb = myclient['Karmel-stg']

#path = '/home/basic-user/nowy/nowy/'
#fs = gridfs.GridFS(mydb)

#url = "http://146.59.80.120:5000/api/v1/downloadName/"

event_collection = mydb['events']

event = 	{
  "events": 
    {
      "events": "123",
      "title": "Dni skupienia w Wadowicach",
      "link": "url",
      "description": "Opis",
      "start_date": "2022/02/13:12:00",
      "end_date": "2022/02/14:14:00",
      "event_type": {
        "id_t": "OCDS",
        "name": "Świecki Zakon",
        "color_code": "green",
      },
      "location": {
        "name": "Klasztor w wadowicach",
        "address": "ul. Jana Pawła",
        "lat": "50.213",
        "lng": "50.513"
      }
    }
  
}

y = event_collection.insert_one(event).inserted_id
'''