  1 #!/usr/bin/python
  2 
  3 import mysql.connector
  4 from mysql.connector import Error
  5 
  6 try:
  7     connection = mysql.connector.connect(host='senanito85.mysql.pythonanywhere-services.com',
  8                                          database='senanito85$cgl',
  9                                          user='senanito85',
 10                                          password='PutHereThePassword')
 11 
 12     sql_select_Query = "select * from laptop"                                                                                                                                       
 13     cursor = connection.cursor()
 14     cursor.execute(sql_select_Query)
 15     records = cursor.fetchall()
 16     print("Total number of rows in Laptop is: ", cursor.rowcount)
 17 
 18     print("\nPrinting each laptop record")
 19     for row in records:
 20         print("Id = ", row[0], )
 21         print("Name = ", row[1])
 22         print("Price  = ", row[2])
 23         print("Purchase date  = ", row[3], "\n")
 24 
 25 except Error as e:
 26     print("Error reading data from MySQL table", e)
 27 finally:
 28     if (connection.is_connected()):
 29         connection.close()
 30         cursor.close()
 31         print("MySQL connection is closed")
