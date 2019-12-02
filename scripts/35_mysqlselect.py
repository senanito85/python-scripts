#!/usr/bin/python

import mysql.connector
from mysql.connector import Error
#Getting user Input
username = input("tell me the username: ")
password = input("tell me the password: ")
#Creating DB connection
try:
    connection = mysql.connector.connect(host='senanito85.mysql.pythonanywhere-services.com',
                                         database='senanito85$cgl',
                                         user='senanito85',
                                         password='<PutPasswordHere>')
    sql_select_Query = "select username, password from User"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)
    print("\nCheking username record")
    for row in records:
        dbuserentry = row[0]
        dbpasswordy = row[1]
        if username == dbuserentry:
            if password == dbpasswordy:
                print("Access Granted")
                print("Welcome",username)
            else:
                print ("Sorry Username or Password is incorrect")
            #print ("username True: ", username)
        else:
            print ("*")
        #print(dbuserentry)
except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
