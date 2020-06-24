# fetch and insert into another table

import cursor as cursor
import mysql.connector
# Establish MySQL database Connection from Python
connection = mysql.connector.connect(host='localhost', port = 3306,
                                         database='ecommerce',
                                         user='root',
                                         password='')

# Define the SELECT statement query. Here you need to know the table, and it’s column details.

cursor.execute('select * from customers')
for row in cursor.fetchall():
# If you wanted all of the data to pass through Python, you could do the following:
    cursor.execute ('insert into mycustomer values ' + str(tuple(row)))

cursor.execute('insert into mycustomer (CustomerID, CustomerName, ContactName, Address, City,PostalCode, Country) select CustomerID, CustomerName, ContactName, Address, City,PostalCode, Country, now() from customers')