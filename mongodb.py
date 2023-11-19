import pymongo

class MongoDBHelper:

    def __init__(self, collection='customerfood'):
        # Replace with your MongoDB connection URI
        uri = "mongodb://localhost:27017"  # Update with your MongoDB URI
        client = pymongo.MongoClient(uri)
        self.db = client['fooddelivery']  # Use your specific database name
        self.collection = self.db[collection]
        print("MongoDB Connected")

    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document Inserted:", result)
        return result  # Return the result for checking success

    def fetch(self, query=None):
        documents = list(self.collection.find(query))
        return documents

    # Other methods for delete, update, etc. can be added here

if __name__ == "__main__":
    main()
