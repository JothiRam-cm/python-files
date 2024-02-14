from pymongo import MongoClient
client=MongoClient('localhost',27017)
database=client['JRDB']
collection=database['services']
# update function
filter={"name":"emailmarketing"}
collection.update_one(filter,{"$set": {"cost":1500}})
print(collection.find_one({"name":"emailmarketing"}))
f={"name":"socialmedia"}
result=collection.update_many(f,{"$set":{"cost":2500}})
print(result.modified_count)
cursor=collection.find({"name":"socialmedia"})
for e_D in cursor:
    print(e_D)