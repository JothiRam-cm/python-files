from pymongo import MongoClient
client= MongoClient('localhost',27017)
database=client['JRDB']
collection=database['services']
#print(collection.find_one)
cursor=collection.find()
for each_doc in cursor:
    print(each_doc)