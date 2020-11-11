# This lesson will include connection to our SQL DB from Python using PYODBC

# pyodbc driver from microsoft helps us to connect to SQL instance
# we will connect to our Northwind DB which you have already used in SQL week

import pyodbc

# class Pyodbc_Connection:
#     def __init__(self):
server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"

# server name - database name - username and password is required to connect to pyodbc
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Cursor is location of your mouse/current path
cursor = northwind_connection.cursor()


# In our DB we have a table called Customers that has customers data available
cust_row = cursor.execute("SELECT * FROM Customers;").fetchall()

# fetchall() method can get all the data available inside our Customers
# BUT fetchall() is default so no need to write it
for records in cust_row:
    print(records)

# We have another table in the DB called Products
product_rows = cursor.execute("SELECT * FROM Products;")
# Running queries in our python program to access database and table inside DB
for records in product_rows:
    # Iterate through the table data and find the unit prices
    print(records.UnitPrice)

product_row = cursor.execute("SELECT * FROM Products;")
# getting the Product table data

# Iterating through the data until the last line of the data (until condition False)
# Combining loop and control flow to ensure we only iterate through the data
# as long as the data is available
while True:
    records = product_row.fetchone()
    if records is None:
        # When there is no records left (value is None) ==> stop
        break
    print(records.UnitPrice)
