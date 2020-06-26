from etl.helper import *

dir = "C:\\Users\\eshet\\OneDrive\\Desktop\\etl\\"
csv_file_path =dir  + "customers_csv.txt"
json_file_path =dir  + "customers_json.txt"

db_host = 'localhost'
db_name_read ='ecommerce'
db_read_query ='SELECT * FROM customers'

db_name_write ='datamart'


# transform data list
mart_list = [] # will hold (name, address)

# extract from csv, json and database  and transofrm
mart_list = mart_list + read_from_csv(csv_file_path)
mart_list = mart_list + read_from_json(json_file_path)
mart_list = mart_list + read_from_databse(db_read_query, database=db_name_read)

# load to datamart
write_into_databse(mart_list, database=db_name_write)



