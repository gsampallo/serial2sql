import serial
from DatabaseControl import DatabaseControl
import json
import os
import sys

class serial2sql:

    def __init__(self,param):
        print("inicio")
        self.parameters = param
        self.output = False
        self.loadParameters()

    def loadParameters(self):
        with open(self.parameters)as f:
            self.param = json.load(f)

        self.dbC = DatabaseControl(self.param)
        self.dbC.createTable()

    def setOutput(self,outputFile):
        self.dbC.setOutPutFile(outputFile)

    def run(self):
        t = [1,1]
        t1 = [2,1]
        t2 = [3,1]
        
        self.dbC.insertData(t)
        self.dbC.insertData(t1)
        self.dbC.insertData(t2)

    # def main(argv):
    #     self.parameters = param
    #     self.loadParameters()

def doc():
    print("Please check documentation: https://github.com/gsampallo/serial2sql")

if __name__ == "__main__":
    if(len(sys.argv[1:]) == 0):
        if os.path.exists("config1.json"):       
            s = serial2sql("config.json")
            #main("config.json")
        else:
            print("config.json not found.")
            doc()
    else:
        if(sys.argv[1] == '-o'):
            if(len(sys.argv[1:]) >= 2):
                s = serial2sql("config.json")
                s.setOutput(sys.argv[2])
            else:
                print("Missing output file")
                doc()