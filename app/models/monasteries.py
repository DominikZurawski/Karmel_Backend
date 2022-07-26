# mongo-engine packages
from mongoengine import *

KIND = ('Sisters', 'Brothers')
        #(('S', 'Sisters'),
        #('B', 'Brothers '))
EVENTS = ("Rekolekcje")

class Monasteries(Document):
    id_monastery = IntField(unique=True) #IntField(required=True)
    name = StringField(max_length=240)
    province = StringField() #URLField() 
    diocese = StringField()
    monastery_kind = StringField(max_length=8, choices=KIND)
    description = StringField() #DateTimeField()
    monastery_call = StringField() #DateTimeField()
    address = StringField()
    website = StringField()
    email = StringField()
    telephone = StringField()
    fax = StringField()
    geopoint = GeoPointField() #PointField()
    pictures = ListField(StringField())

    events = ListField(StringField())

    

    