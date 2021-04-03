#!/usr/bin/python3
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="noroot",
    password="noroot",
    database="Colegio"
)

myCursor=mydb.cursor()

myCursor.execute("CREATE TABLE customers (name VARCHAR(244), address VARCHAR(255))")
