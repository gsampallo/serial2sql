
from datetime import datetime, timedelta
import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'usuario1',
    'password': 'DemoDemo%1810',
    'host': 'localhost',
    'database': 'data',
    'raise_on_warnings': True,
}

class DatabaseControl:

    def __init__(self,fields):
        self.fields = fields
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()        

    def createTable(self,tableName):
        self.tableName = tableName
        sqlDrop = "DROP TABLE IF EXISTS `"+config['database']+"`.`"+self.tableName+"`"

        #print(sqlDrop)
        sql = "CREATE TABLE "+self.tableName+" (id INT(9) NOT NULL AUTO_INCREMENT"
        for field in self.fields:
            sql = sql+","+field['name']+" "+field['type']
        sql = sql + ",PRIMARY KEY (id))"
        #print(sql)
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
        
        self.sqlInsert = "INSERT INTO "+self.tableName+" ("+self.fields[0]['name']

        for i in range(1,len(self.fields)):
            self.sqlInsert = self.sqlInsert+","+self.fields[i]['name']
        self.sqlInsert = self.sqlInsert + ") VALUES ("+("%s,"*(len(self.fields) -1))+"%s"+")"


    def getInsertDataSQL(self):
        print(self.sqlInsert)    


    def insertData(self,data):
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

