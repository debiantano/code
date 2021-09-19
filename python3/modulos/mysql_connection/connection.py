 #!/usr/bin/python3
 import mysql.connector

 mydb=mysql.connector.connect(
     host="localhost",
     user="noroot",
     password="noroot"
 )

 myCursor=mydb.cursor()

 myCursor.execute("SHOW DATABASES")

 for x in myCursor:
     print(x)
