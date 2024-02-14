from pymongo import MongoClient
client=MongoClient('localhost',27017)
database=client['JRDB']
collection=database['services']
#deletion function
collection.delete_one({"name":"SEO"})
filter={"name":"emailmarketing"}
result=collection.delete_many(filter)
print(result.deleted_count)
cursor=collection.find()
for E_D in cursor:
    print(E_D)
    