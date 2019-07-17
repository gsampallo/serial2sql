
from datetime import datetime, timedelta
import mysql.connector
from mysql.connector import errorcode
import json
import io
import os

class DatabaseControl:

    def __init__(self,config):
        self.output = False
        self.config = config
        self.cnx = mysql.connector.connect(user=config["credentials"]["user"],database=config["credentials"]["database"],password=config["credentials"]["password"])
        self.cursor = self.cnx.cursor()        

    def createTable(self):
        #self.tableName = tableName
        tableName = self.config["tableName"]
        sqlDrop = "DROP TABLE IF EXISTS `"+self.config["credentials"]["database"]+"`.`"+tableName+"`;"

        #print(sqlDrop)
        sql = "CREATE TABLE "+tableName+" (id INT(9) NOT NULL AUTO_INCREMENT"
        fields = self.config["fields"]
        for field in fields:
            sql = sql+","+field['name']+" "+field['type']
        sql = sql + ",PRIMARY KEY (id))"
        print(sql)


        if(not self.output):
            try:
                #self.cursor.execute(sqlDrop)
                self.cursor.execute(sql)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)        
        else:
            if(self.outputFile.find("sql") > 0):
                file = open(self.outputFile,"a")
                file.write(sql+";\n")
                file.close()           

        self.sqlInsert = "INSERT INTO "+tableName+" ("+fields[0]['name']

        for i in range(1,len(fields)):
            self.sqlInsert = self.sqlInsert+","+fields[i]['name']
        self.sqlInsert = self.sqlInsert + ") VALUES ("+("%s,"*(len(fields) -1))+"%s"+")"


    def getInsertDataSQL(self):
        print(self.sqlInsert)    

    def setOutPutFile(self,outputFile):
        self.output = True
        self.outputFile = outputFile
        if os.path.exists(outputFile):    
            os.remove(outputFile)


    def saveToFile(self,data):
        
        if(self.outputFile.find("sql") > 0):
            sql = self.sqlInsert
            data1 = str(data).strip("[]").split(",")
            sql = sql % tuple(data1)+";\n"
            file = open(self.outputFile,"a")
            file.write(sql)
            file.close()
        elif(self.outputFile.find("csv") > 0):
            file = open(self.outputFile,"a")
            file.write(str(data).strip("[]")+"\n")
            file.close()

    def saveToDataBase(self,data):
        try:
            self.cursor.execute(self.sqlInsert,data)
            self.cnx.commit()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err) 
          
    def insertData(self,data):
        print(data)        
        if(self.output):
            self.saveToFile(data)
        else:
            self.saveToDataBase(data)

