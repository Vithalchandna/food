import mysql.connector as db

class Customer:
    def _init_(self):
        self.name = input("Enter customer name:")
        self.phone = input("Enter customer phone:")
        self.email = input("Enter customer email:")

def main():
    customer = Customer()
    print(vars(customer))
    connection = db.connect(user='root', password='vithal', host='127.0.0.1', database='mydatabase')
    cursor = connection.cursor()
    sql = "INSERT INTO Customer values" "(null,'{name}','{phone}','{email}');".format_map(vars(customer))
    cursor.execute(sql)
    connection.commit()
    print("Customer inserted")

if _name_ == "_main_":
 main()