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

        print("Port: ",self.param["port"])
        print("Baudrate: ",self.param["baudrate"])

        for field in self.param["fields"]:
            print("Field: ",field["name"]," type: ",field["type"])

