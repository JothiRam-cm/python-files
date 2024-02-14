from pymongo import MongoClient

client = MongoClient('localhost',27017)

database=client['JRDB']
print("database created")
collection=database['services']
print("collection is created ")
services=[
    {"name":"emailmarketing","cost":1000},
    {"name":"socialmedia","cost":2000},
    {"name":"SEO","cost":3100}]
result=collection.insert_many(services)
print(result.inserted_ids)