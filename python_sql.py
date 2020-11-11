# This lesson will include connection to our SQL DB from Python using PYODBC

# pyodbc driver from microsoft helps us to connect to SQL instance
# we will connect to our Northwind DB which you have already used in SQL week
import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"

northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# server name - database name - username and password is required to connecto to pyodbc
cursor = northwind_connection.cursor()


cursor.execute("SELECT @@VERSION")
raw = cursor.fetchone()
print(raw)