#!/usr/bin/python3
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="noroot",
    password="noroot",
    database="Colegio"
)

myCursor=mydb.cursor()

myCursor.execute("SHOW TABLES")

for x in myCursor:
    print(x)
