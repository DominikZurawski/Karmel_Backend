# mongo-engine packages
from mongoengine import *
from models.monasteries import Monasteries

'''class Event_Type(Document):
    id_t = StringField()
    name = StringField()
    color_code = StringField()

class Location(Document):
    name = StringField()
    address = StringField()
    lat = StringField()
    lng = StringField()'''

class Events(Document):
    id_event = IntField(unique = True)
    title = StringField(max_length=240)
    link = StringField() #URLField() 
    description = StringField()
    start_date = DateTimeField()
    end_date = DateTimeField()
    event_type = DictField()#, validation = True)
    location = ReferenceField(Monasteries)

    

    