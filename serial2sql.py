import serial
from DatabaseControl import DatabaseControl
import json

class serial2sql:

    def __init__(self,param):
        print("inicio")
        self.parameters = param
        self.loadParameters()

    def loadParameters(self):
        with open(self.parameters)as f:
            self.param = json.load(f)

        self.dbC = DatabaseControl(self.param["fields"])
        self.dbC.createTable(self.param["tableName"])

    def run(self):
        t = [1,1]
        t1 = [2,1]
        t2 = [3,1]
        
        self.dbC.insertData(t)
        self.dbC.insertData(t1)
        self.dbC.insertData(t2)

