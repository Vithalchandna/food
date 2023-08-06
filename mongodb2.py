import datetime
class Customer:
    def __init__(self):
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
        self.createdon = datetime.datetime.today()