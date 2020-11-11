import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
connection = pyodbc.connect(
    f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"
)
cursor = connection.cursor()

query = "SELECT CustomerID FROM Customers WHERE City = ?"
with cursor.execute(query, "London"):
    row = cursor.fetchone()
    while row:
        print(f"{str(row[0])}")
        row = cursor.fetchone()