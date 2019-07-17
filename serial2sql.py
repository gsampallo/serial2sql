import serial
from serial import SerialException
from DatabaseControl import DatabaseControl
import json
import os
import sys

class serial2sql:

    def __init__(self,param):
        self.parameters = param
        self.output = False
        self.loadParameters()

    def loadParameters(self):
        with open(self.parameters)as f:
            self.param = json.load(f)

        self.dbC = DatabaseControl(self.param)
        #self.dbC.createTable()

    def setOutput(self,outputFile):
        self.dbC.setOutPutFile(outputFile)

    def run(self):
        self.dbC.createTable()
        print("Opening port and starting to save data")
        print("Press Ctrl+C to stop")
        try:
            ser = serial.Serial(self.param["port"], self.param["baudrate"], timeout=1)
            while(True):

                line = str(ser.readline()).replace("\r\n","")
                if(len(line)> 0):
                    if(line.find(",")):
                        data = line.split(",")
                        self.dbC.insertData(data)
        except SerialException as se:
            print("Error when tried to open the port")
            print(se)

        except Exception as e:
            print("Error when tried to open the port")
            print(e)
        


def doc():
    print("Use only serial2sql.py to save data to database.")
    print("If you use the -o parameter, needs to add the name of file where you wants to save the data.")
    print("Please check documentation: https://github.com/gsampallo/serial2sql")

if __name__ == "__main__":
    
    if (not os.path.exists("config.json")): 
        print("config.json not found.")
        doc()
        exit()
    else:
        if(len(sys.argv[1:]) == 0):   
            s = serial2sql("config.json")
        elif(sys.argv[1] == '-o'):
            if(len(sys.argv[1:]) >= 2):
                s = serial2sql("config.json")
                s.setOutput(sys.argv[2])
            else:
                print("Missing output file")
                doc()
                exit()
        s.run()
