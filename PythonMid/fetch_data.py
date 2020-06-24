import random

import mysql.connector

connection = mysql.connector.connect(host='localhost', port = 3306,
                                         database='ecommerce',
                                         user='root',
                                         password='')

sql_select_Query = "select * from customers"
cursor = connection.cursor()
cursor.execute(sql_select_Query)
