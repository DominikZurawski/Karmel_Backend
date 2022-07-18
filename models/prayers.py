# mongo-engine packages
from mongoengine import *

class Prayers(Document):   
    date = DateTimeField() #ComplexDateTimeField(required=True))
    content = ListField()  

