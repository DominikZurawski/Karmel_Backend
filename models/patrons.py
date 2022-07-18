# mongo-engine packages
from mongoengine import *
from PIL import Image


class Patrons(Document):
    patron = StringField(unique=True, max_length=240)
    description = StringField()
    image = ImageField()
    url_image = StringField()
    quotes = ListField() 
    url = StringField() 


    
