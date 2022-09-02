# mongo-engine packages
from mongoengine import *
from PIL import Image


class Patrons(Document):
    patron = StringField(unique=True, max_length=240)
    description = StringField()
    url = StringField()      
    quotes = ListField()
    siglum = ListField() 


    
