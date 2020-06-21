import random

import mysql.connector

connection = mysql.connector.connect(host='localhost', port = 3306,
                                         database='ecommerce',
                                         user='root',
                                         password='')

sql_select_Query = "select * from customers"
cursor = connection.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
applicants = {}
quota = 20
ids = []
winner_ids=[]
for r in records:
    ids.append(r[0])
    applicants[r[0]] = r

    print(r)
c =1
for  c in range(0, quota):
    winner_index = random.randint(0, len(ids) - 1)
    winner = ids[winner_index]
    winner_ids.append(winner)
    ids.remove(winner)

# print winer info
print("*"*10 + "DV 2020 winners ")
for record in records :
    if record[0] in winner_ids:
        print(record)
        #  mail to the winner


final_record = records + records

#  connect o your database
# inserter selceted records to the deatabs e

for winner in winner_ids:
    print(applicants[winner])
