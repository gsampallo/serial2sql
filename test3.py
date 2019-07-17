from serial2sql import serial2sql

s = serial2sql("config.json")
s.setOutput("output.sql")
s.run()