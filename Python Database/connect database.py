import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)
print(mydb)
# create the database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE SUPER")

# Check if the database exist
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
