import datetime

"""
    Pet: pid, name, age, weight, breed, gender, cid, createdon
    create table Customer(
        cid int primary key auto_increment,
        name text,
        phone text unique key,
        email text,
        age int,
        gender text,
        address text,
        createdon datetime
    );

    create table Pet(
        pid int primary key auto_increment,
        name text,
        age int,
        weight int,
        breed text,
        gender text,
        cid int,
        createdon datetime,
        FOREIGN KEY (cid) REFERENCES Customer(cid)
    );
"""


class Pet:

    def __init__(self):
        self.pid = 0
        self.name = ""
        self.age = 0
        self.weight = 0
        self.breed = ""
        self.gender = ""
        self.cid = 0
        self.createdon = ""

    def read_pet_data(self):
        self.name = input("Enter Pet Name: ")
        self.age = int(input("Enter Pet Age: "))
        self.weight = int(input("Enter Pet Weight: "))
        self.breed = input("Enter dog breed: ")
        self.gender = input("Enter Pet Gender (male/female): ").lower()

        # Get the date and time
        self.createdon = str(datetime.datetime.today())
        # Eliminate Milli Seconds
        self.createdon = self.createdon[: self.createdon.rindex(".")]

    def get_insert_sql_query(self):
        sql = "insert into pet values(null,'{name}',{age},{weight}"\
               "'{breed}','{gender}',{cid},'{createdon}');".format_map(vars(self))
        return sql





    def get_insert_sql_query(self):
        sql = "insert into Customer values(null, '{name}', '{phone}', '{email}', {age}, " \
              "'{gender}', '{address}', '{createdon}');".format_map(vars(self))
        return sql
    def get_customers_sql_query(self, phone=""):
        if len(phone) == 0:
            sql = "select * from Customer"
        else:
            sql = "select * from Customer where phone = '{}'".format(phone)
        return sql
    def get_delete_sql_query(self):
        sql = "delete from Customer where cid = {}".format(self.cid)
        return sql
    def get_update_sql_query(self):
        sql = "update Customer set name='{name}', phone='{phone}', email='{email}', age={age}, " \
              "gender='{gender}', address='{address}' where cid = {cid}".format_map(vars(self))
        return sql

