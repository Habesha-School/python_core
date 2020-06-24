# Establish MySQL database Connection from Python
import mysql.connector

conn = mysql.connector.connect(host='localhost', port = 3306,
                                         database='ecommerce',
                                         user='root',
                                         password='')

# creating a cursor object using the cursor() method
cursor = conn.cursor()

# Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS MYEMPLOYEE")

# Creating table as per requirement
sql_create_Query = '''CREATE TABLE MYEMPLOYEE(
   EmployeeID int(11) NOT NULL,
   LastName varchar(50) NOT NULL,
   FirstName varchar(50) NOT NULL,
   BirthDate DATE NOT NULL,
   Notes varchar(100),
   Photo LONGBLOB 
)'''
cursor.execute(sql_create_Query)

# Preparing SQL query to INSERT a record into the database.
sql_insert_Query = """INSERT INTO MYEMPLOYEE(
   EmployeeID, LastName, FirstName, BirthDate, Notes, Photo)
   VALUES (11, 'Eshete', 'Tesfaye', ' ', 'Manager', '')"""
cursor.execute(sql_insert_Query)

# Define the SELECT statement query. Here you need to know the table, and it’s column details.
sql_select_Query = "select * from MYEMPLOYEE"
cursor.execute(sql_select_Query)
records = cursor.fetchall()
print("Total number of rows in MYEMPLOYEE is: ", cursor.rowcount)
print("Printing each customer record")
for row in records:
    print("EmployeeID", row[0],"LastName", row[1], "FirstName", row[2], "BirthDate",  row[3], "Notes", row[4], "Photo", row[5])

#Closing the connection
conn.close()