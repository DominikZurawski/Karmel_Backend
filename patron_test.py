import pymongo
from PIL import Image

from mongoengine import *

connect = connect(host="mongodb://mongoAdmin:M3hGjZXfQdp53XVL@localhost:27017/Karmel-stg?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")

class Patrons(Document):
    patron = StringField(unique=True, max_length=240)
    description = StringField()
    image = ImageField()
    url_image = StringField()
    quotes = ListField() 
    url = StringField() 

downl_image = "http://146.59.80.120:5000/api/v1/PatronImage/"
filename = 'Teresa od Dz. Jezus'
name = 'Teresa od Dz. Jezus'
l = Patrons(patron=name)
l.save()

opis = 'Jan od Krzyża Ojciec Karmelu'

i = Patrons.objects(patron=name).get()

i.description = opis
i.url = "https://www.karmel.pl/swieta-teresa-od-dzieciatka-jezus-teresa-martin-1873-1897/"
i.image.put(open('/home/basic-user/herb.jpg', 'rb'), filename = filename )#+ ".jpg" )
i.url_image = downl_image + filename #+ ".jpg"

for n in range(0, 60):
	d = "Cytat "+ str(n)
	i.quotes.append(d)

i.save()




