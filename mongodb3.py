import pymongo
from tabulate import tabulate

class MongoDBHelper:

    def __init__(self, collection='customerfoood'):
        uri = "mongodb+srv://vithalchandna:root123@cluster0.zzl8oin.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri)
        self.db = client['abc']
        self.collection = self.db[collection]
        print("MongoDB Connected")

    def insert(self, data):
        result = self.collection.insert_one(data)
        return result

    def delete(self, query):
        result = self.collection.delete_one(query)
        print("Document Deleted:", result)

    def fetch(self, query=""):
        documents = self.collection.find(query)
        # for document in documents:
        #     print(document)
        return list (documents)


        # print(tabulate(documents, headers="keys", tablefmt="grid"))
