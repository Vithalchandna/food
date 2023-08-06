import datetime
from
class Consultant:
    def __init__(self):
        self.cnid = 0
        self.cid = 0
        self.pid = 0
        self.problem = ""
        self.heartrate = 0
        self.temperate = 98.4
        self.createdon = ""

    def read_consultant_data(self):
        self.problem = input("enter the problem")
        self.heartrate = int(input("enter the heart rate"))
        self.temperate = float(input("enter temperate"))
        self.medicines = input("enter the medicines")
        self.createdon = str(datetime.datetime.today())
        self.createdon = self.createdon[self.createdon.rindex()]

    def get_insert_sql_query(self):
        sql = "insert into Consultant values(null,{cid},{pid},'{problem}',"\
              "{heartarte},{temperate},'{medicines}','{createdon}');",format_map(vars(self))
        return sql

    def get_consultant_sql_query(selfself,cid="",pid=""):
        sql = "select * from Consultant"
        if len(cid) != 0
            sql = "select * from Consultant where cid ={}.format(cid)"






