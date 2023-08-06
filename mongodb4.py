from mongodb2 import Customer
from mongodb3 import MongoDBHelper
from bson.objectid import ObjectId
def main():
      db = MongoDBHelper()


      #customer = Customer()
      #customer.read_customer_data()

      #document = vars(customer)
      #db.insert(document)

      query = {'phone': '+91 854548454'}
      #query = {'_id': ObjectId('64c513a7f43099791aa78e2a')}
      #db.delete(query)

      #db.fetch()
      db.fetch(query=query)

      document = {'name': 'Raman' , 'age': 18}
      db.update(document,query)

if __name__ == "__main__":
      main()