"""reading from csv"""
import csv
import json

import mysql.connector

def read_from_csv(file_path):
    mart_list_temp =[]
    # extracting data from csv
    with open(file_path) as from_file:
        readCSV = csv.reader(from_file, delimiter=',')
        # parse through each line, get name and address and add into temp mart list
        for row in readCSV:
            selected_colums =(row[1], row[3])
            print(selected_colums)
            mart_list_temp.append(selected_colums)
        return mart_list_temp

def read_from_json(file_path):
    mart_list_temp=[]
    # extract data from json
    with open(file_path) as from_file:
      data = json.load(from_file)
      print(data)
      data = data[2]["data"]
      for record  in data:
          selected_colums  =(record["CustomerName"], record["Address"])
          mart_list_temp.append(selected_colums)

      return mart_list_temp

 # read from xml

 # read from excell

def read_from_databse(query, host='localhost', port=3306, database='ecommerce', user='root', password=''):

    # read from database
    # connect to the given database
    connection = mysql.connector.connect(host=host, port = port,
                                             database=database,
                                             user=user,
                                             password=password)

    mart_list_temp=[]
    # excute the given query
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    # extract selected records and ad into temp mart list
    for record in data:
        selected_colums = (record[1], record[3])
        mart_list_temp.append(selected_colums)

    return  mart_list_temp


def write_into_databse(mart_list, host='localhost', port=3306, database='datamart', user='root', password=''):
    # load to database
    # connect to the given database
    connection = mysql.connector.connect(host=host, port=port,
                                         database=database,
                                         user=user,
                                         password=password)

    table = 'combined'
    cursor = connection.cursor()
    # clear records from the table
    cursor.execute("TRUNCATE TABLE {}".format(table))

    sql = "INSERT INTO {} (name, address) VALUES (%s, %s)".format(table)
    for val in mart_list:
        cursor.execute(sql, val)

    connection.commit()

