"""
    mongodb.com
    1. Create Account on MongoDB Atlas
    2. Network Access -> 0.0.0.0/0
    3. Create DataBase user and password
    4. Navigate to Browse Collections > Create DataBase and a Colellction
    Reference Documentation -> https://pymongo.readthedocs.io/en/stable/
    pip install pymongo
    pip install pymongo[srv]
    If facing SSL certificate error
"""


#import certifi # pip install certifi | If SSL error

# ca = certifi.where() # If SSL error
import pymongo
uri = "mongodb+srv://vithalchandna:root123@cluster0.zzl8oin.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
# client = pymongo.MongoClient(uri, tlsCAFile=ca) # If SSL error
db = client['pythontraining']
collections = db.list_collection_names()
# print(collections)

for collection in collections:
    print(collection)

documents = db['customer'].find()
for document in documents:
    print(document)