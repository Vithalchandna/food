import pymongo
#import certifi # pip install certifi | If SSL error

# ca = certifi.where() # If SSL error

uri = "mongodb+srv://vithalchandna:root123@cluster0.zzl8oin.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
# client = pymongo.MongoClient(uri, tlsCAFile=ca) # If SSL error
db = client['cutomerfood']
collections = db.list_collection_names()
# print(collections)

for collection in collections:
    print(collection)

#documents = db['students'].find()
#for document in documents:
  #  print(document)