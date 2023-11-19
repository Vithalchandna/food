import pymongo
from tabulate import tabulate
from pymongo import mongo_client

class MongoDBHelper:

    def _init_(self, collection='customerfood'):
        uri = "mongodb+srv://vithalchandna:root123@cluster0.zzl8oin.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri)
        self.db = client['fooddelivery']
        self.collection = self.db[collection]
        print("MongoDB Connected")

    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document Inserted:", result)
        # result.inserted_id -> Document Id
        return result

    def delete(self, query):
        result = self.collection.delete_one(query)
        print("Document Deleted:", result)

    def fetch(self, query=""):
        documents = self.collection.find(query) # find_one()
        return list(documents)

    def update(self, document, query):
        update_query = {'$set': document}
        result = self.collection.update_one(query, update_query)
        print("Updated Document:", result.modified_count)