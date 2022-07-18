import pymongo
#myclient = pymongo.MongoClient("mongodb://mongoAdmin:M3hGjZXfQdp53XVL@146.59.80.120:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
myclient = pymongo.MongoClient("mongodb://mongoAdmin:M3hGjZXfQdp53XVL@localhost:27017/Karmel-stg?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
#myclient = pymongo.MongoClient("mongodb://mongoAdmin:M3hGjZXfQdp53XVL@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
#myclient = pymongo.MongoClient("mongodb+srv://domin:5MorGulis8@cluster0.ltlh4.mongodb.net/Karmel?retryWrites=true&w=majority")
#myclient = pymongo.MongoClient("mongodb://mongoAdmin:M3hGjZXfQdp53XVL@getstarted-ec2.cluster-coixp3sqt71k.eu-central-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false")
mydb = myclient.test
mydb = myclient['Karmel-stg']

patrons_collection = mydb['patrons']

patron = 	{
		  "patron": {
		    "name": "Teresa od Jezusa"
		  },
		  "quotes": [
		    "Cytat 1",
		    "Cytat 2"
		  ]
		}

x = patrons_collection.insert_one(patron).inserted_id

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



monastery_collection = mydb['monasteries']

monastery = 	{
  "monasteries": 
    {
      "id": "123",
      "name": "Klasztow w wadowicach",
      "province": "Warszawska",
      "monastery_kind": "brothers | sisters",
      "description": "Opis",
      "monastery_call": "Pod wezwaniem Św Józefa",
      "address": "ul. Jana Pawła",
      "lat": "50.213",
      "lng": "50.513",
      "events": [],
      "pictures": ["url"]
    }
  
}

z = monastery_collection.insert_one(monastery).inserted_id

prayer_collection = mydb['prayers']

prayer = 	{
  "audio": {
    "id": "trackId",
    "url": "url.mp3",
    "title": "Track Title"
  },
  "text": {
    "gospel": {},
    "contemplation": "tekst",
    "questions": [
      "Jeden",
      "Dwa"
    ]
  }
}

z = prayer_collection.insert_one(prayer).inserted_id







