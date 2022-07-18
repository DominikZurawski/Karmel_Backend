import pymongo
from datetime import datetime
import gridfs
from mongoengine import *
from flask import Response, request, jsonify

import json
from bson import json_util

from urllib.request import urlopen

myclient = pymongo.MongoClient("mongodb://mongoAdmin:M3hGjZXfQdp53XVL@localhost:27017/Karmel-stg?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
mydb = myclient.test
mydb = myclient['Karmel-stg']
prayer_collection = mydb['prayers']
path = '/home/basic-user/nowy/nowy/'
fs = gridfs.GridFS(mydb)

url = "http://146.59.80.120:5000/api/v1/downloadName/"

prayer = 	{
      "date": datetime.now(),                      
      "content" :[{
                "filename": 'Ow02_czw_30_04.mp3',
                "url" : url + 'Ow02_czw_30_04.mp3',
                "file": fs.put(open(path+'Ow02_czw_30_04.mp3', 'rb'), filename='Ow02_czw_30_04.mp3'),
                "description": "Ewangelia według świętego Jana ...",
                },
                {

                "filename": 'Ow02_czw_41_04.mp3',
                "url" : url + 'Ow02_czw_41_04.mp3',
                "file": fs.put(open(path+'Ow02_czw_41_04.mp3', 'rb'), filename='Ow02_czw_41_04.mp3'),
                "description": "question1",
                },
                {

                "filename": 'Ow02_czw_42_04.mp3',
                "url" : url + 'Ow02_czw_42_04.mp3',
                "file": fs.put(open(path+'Ow02_czw_42_04.mp3', 'rb'), filename='Ow02_czw_42_04.mp3'),
                "description": "question2",
                },
                {

                "filename": 'Ow02_czw_43_04.mp3',
                "url" : url + 'Ow02_czw_43_04.mp3',
                "file": fs.put(open(path+'Ow02_czw_43_04.mp3', 'rb'), filename='Ow02_czw_43_04.mp3'),
                "description": "question3",
                },
                {

                "filename": 'Ow02_czw_43_04.mp3',
                "url" : url + 'Ow02_czw_43_04.mp3',
                "file": fs.put(open(path+'Ow02_czw_43_04.mp3', 'rb'), filename='Ow02_czw_43_04.mp3'),
                "description": "question4",
                },
      ],      
    }

z = prayer_collection.insert_one(prayer).inserted_id
