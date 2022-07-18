import pymongo
from datetime import datetime
import gridfs

myclient = pymongo.MongoClient("mongodb://mongoAdmin:M3hGjZXfQdp53XVL@localhost:27017/Karmel-stg?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
mydb = myclient.test
mydb = myclient['Karmel-stg']
prayer_collection = mydb['prayers']

#name = '/home/basic-user/nowy/Oz_1_wt_41.mp3'
#filedata = open(name, 'rb')
#data = filedata.read()
'''
fs = gridfs.GridFS(mydb)
name = '/home/basic-user/nowy/Oz_1_wt_41.mp3'
data = mydb.fs.files.find_one({'filename':name})
print(data)

myid=data['_id']
outputdata=fs.get(myid).read()
output= open("file.mp3", 'wb')
output.write(outputdata)
output.close()
print('download complete')

#fs.put(data, filename=name)
'''

fs = gridfs.GridFS(mydb)

name = 'Ow02_czw_30_04.mp3'
data = mydb.fs.files.find_one({'filename':name})
print(data)

myid=data['_id']
outputdata=fs.get(myid).read()
output= open("file1.mp3", 'wb')
output.write(outputdata)
output.close()
print('download complete')