# SQL SELECT Query from Python application to retrieve MySQL table rows and columns

# Use fetchall(), fetchmany() and fetchone()  methods of a cursor class to fetch limited rows from a table

import random

import mysql.connector
# Establish MySQL database Connection from Python
conn = mysql.connector.connect(host='localhost', port = 3306,
                                         database='ecommerce',
                                         user='root',
                                         password='')
# creating a cursor object using the cursor() method
cursor = conn.cursor()

# Define the SELECT statement query. Here you need to know the table, and it’s column details.
sql_select_Query = "select * from customers"

# Execute the SELECT query using the cursor.execute() method.
cursor.execute(sql_select_Query)
# Get resultSet from the cursor object using a cursor.fetchall().
records = cursor.fetchall()

print("Total number of rows in customers is: ", cursor.rowcount)
print("\nPrinting each customer record")
for row in records:
    print("CustomerID", row[0], "CustomerName", row[1], "ContactName", row[1], "Address", row[2], "City", [3], "PostalCode", [4], "Country", [5], "\n")


