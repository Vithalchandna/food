import mysql.connector as db
import datetime

class Customer:
    def _init_(self):
        self.name = ""
        self.phone = ""
        self.email = ""
        self.age = 0
        self.gender = ""
        self.address = ""
        self.createdon = ""

    def read_customer_data(self):
        self.name = input("Enter customer name:")
        self.phone = input("Enter customer phone:")
        self.email = input("Enter customer email:")
        self.age = int(input("Enter customer age:"))
        self.gender = input("Enter customer gender(male/female):").lower()
        self.address = input("Enter customer address:")
        self.createdon = str(datetime.datetime.today())
        self.createdon = self.createdon[: self.createdon.rindex(".")]

    def get_insert_sql_query(self):
        sql = "insert into Customer values(null , '{name}','{phone}','{email}'," \
              "'{age}','{gender}','{address}','{createdon}');".format_map(vars(self))
        return sql
    def main():
      customer = Customer()
      customer.read_customer_data()
      print(vars(Customer))

if __name__ == "_main_":
    main()