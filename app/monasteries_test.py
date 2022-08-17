import pymongo
from PIL import Image

from mongoengine import *

connect = connect(host="mongodb://mongoAdmin:M3hGjZXfQdp53XVL@localhost:27017/Karmel-stg?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")

KIND = ('Sisters', 'Brothers')
		#(('S', 'Sisters'),
        #('B', 'Brothers '))
EVENTS = ("Rekolekcje")

class Monasteries(Document):
    id_monastery = IntField(unique=True) #IntField(required=True)
    name = StringField(max_length=240)
    province = StringField() #URLField() 
    dieesis = StringField()
    monastery_kind = StringField(max_length=8, choices=KIND)
    description = StringField() #DateTimeField()
    monastery_call = StringField() #DateTimeField()
    address = StringField()
    webside = StringField()
    email = StringField()
    telephone = StringField()
    fax = StringField()
    geopoint = GeoPointField() #PointField()
    pictures = ListField(StringField())

    events = ListField(StringField())


_id = 0
M = Monasteries(id_monastery = _id)
M.save()

i = Monasteries.objects(id_monastery= _id).get()
i.name = "Kraków - Śródmieście"
i.province = "Krakowska"
i.dieesis = "Archidiecezja Krakowska"
i.monastery_kind = 'Brothers'
i.description = "W Polsce przedrozbiorowej istniały w Krakowie dwa klasztory karmelitów bosych: Niepokalanego Poczęcia NMP na przedmieściu Wesoła (1605-1787) oraz św. Michała i św. Józefa pod Wawelem (1611-1797). Decyzję o założeniu obecnego klasztoru pw. Niepokalanego Poczęcia NMP podjęło Definitorium Prowincji Austriackiej w roku 1907. W grudniu 1909 r. rozpoczęto w nim życie zakonne. Od 1911 r. klasztor w Krakowie jest siedzibą Kolegium Teologicznego, a w latach 1927-1994 prowadzona przy nim była działalność wydawnicza. /n Kościół jest szczególnym ośrodkiem kultu św. Józefa, patrona miasta Krakowa. Od października 1991 r. przy klasztorze istnieje Karmelitański Instytut Duchowości. W latach 1999-2000 wzniesiono dla nie-go nowy budynek. KID jest stowarzyszony z Papieskim Instytutem Duchowości Teresianum w Rzymie. Współpracuje także z Uniwersytetem Papieskim Jana Pawła II w Krakowie"
i.monastery_call = "Konwent pw. Niepokalanego Poczęcia Najświętszej Maryi Panny"
i.address = "Karmelici Bosi /nul. Rakowicka 18 /n31-510 Kraków"
i.webside = "www.rakowicka18.pl"
i.email = "rakowicka18@gmail.com"
i.telephone = "12 424 04 10"
i.fax = "12 294 45 54"
i.geopoint = [50.0687205485399, 19.95224448139427]

i.pictures = ["https://www.karmel.pl/wp-content/uploads/2016/10/DSC_7266.jpg","https://www.karmel.pl/wp-content/uploads/2016/10/DSC_7280.jpg"]
i.save()


_id = 1000
M = Monasteries(id_monastery = _id)
M.save()

i = Monasteries.objects(id_monastery= _id).get()
i.name = "Kraków-Łobzów"
i.province = "Krakowska"
i.dieesis = "Archidiecezja Krakowska"
i.monastery_kind = 'Sisters'
i.description = "Klasztor ufundowany przez karmelitanki poznańskie wyrzucone z Poznania w okresie Kulturkampfu. Regularne życie zakonne rozpoczęto 1 sierpnia 1875 r. W latach 1903-1904 wybudowany został obecny kościół i klasztor. Karmelitanki z klasztoru łobzowskiego wraz ze swoją fundatorką m. Ksawerą Czartoryską, w wielkiej mierze przyczyniły się do odrodzenia życia karmelitańskiego na ziemiach polskich w drugiej połowie XIX w., przez starania czynione u Generała Zakonu w celu uzyskania pomocy dla odnowy życia zakonnego w jedynym klasztorze ojców w Czernej, poprzez inicjatywę fundacji klasztoru braci w Krakowie oraz przez zabieganie o wstąpienie do Karmelu Józefa Kalinowskiego."
i.monastery_call = "Klasztor pw. Opieki Św. Józefa"
i.address = "Karmelitanki Bose /nul. Łobzowska 40 /n31-140 Kraków"
i.webside = "www.karmelitankikrakow.pl"
i.email = "sskb.santjosef@gmail.com"
i.telephone = "12 633 93 42"
i.geopoint = [50.07093576270597, 19.930684063317067]

i.pictures = ["https://karmel.pl/wp-content/uploads/2016/10/gggg.jpg", "https://www.karmel.pl/wp-content/uploads/2016/08/%C5%82obz%C3%B3w1.jpg"]
i.save()

'''
import pymongo
#from datetime import datetime
#import gridfs
#from mongoengine import *
#from flask import Response, request, jsonify

#import json
#from bson import json_util



myclient = pymongo.MongoClient("mongodb://mongoAdmin:M3hGjZXfQdp53XVL@localhost:27017/Karmel-stg?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
mydb = myclient.test
mydb = myclient['Karmel-stg']
'''
#path = '/home/basic-user/nowy/nowy/'
#fs = gridfs.GridFS(mydb)

#url = "http://146.59.80.120:5000/api/v1/downloadName/"
'''
monastery_collection = mydb['monasteries']

monastery = {
      "id_monastery": 125,
      "name": "Klasztor w Krakowie",
      "province": "Krakowska",
      "monastery_kind": "sisterss",
      "description": "Fajny Opis opis",
      "monastery_call": "Pod wezwaniem ...",
      "address": "Karmelitanki Bose \nul.   \n00-000 Kraków ",
      "lat": "50.213",
      "lng": "50.513",
      "events": [],
      "pictures": ["url"]
    }


z = monastery_collection.insert_one(monastery).inserted_id
'''