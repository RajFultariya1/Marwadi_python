from mysql.connector.cursor import MySQLCursor
import mysql.connector
mycon=mysql.connector.connect(
   host='localhost',
   user='root', 
   password=''   
)
mycursor=mycon.cursor()
mycursor.execute("create database if not exists Marwadi_python")
print('done')
mycon.close()