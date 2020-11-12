# Task:
- Create a new file and class with function to 
establish connection with pyodbc  
- Create a function to get UnitPrice values

- Create a function that creates a table in the DB
- Create a function that prompts user to input data
in that table
- Create a new file called PYODBC_TASK.md and document
the steps of the task

## Solution
- First create the class and setup connection in a method
**We will access the connect method in every method so that its always connected**
```python
import pyodbc

class Pyodbc_Connection:
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "**"
        self.password = "***"


    def connect(self):
        self.northwind_connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        # Cursor is location of your mouse/current path
        self.cursor = self.northwind_connection.cursor()
```
- Get UnitPrice method which displays the unit price in Products Table
```python
    def get_UnitPrice(self):
        self.connect()
        # Prompts the user to select the correct table, in this case the Products
        what_table = input("What table would you like to use?\n -> ").title()
        if what_table == 'Products':
            product_rows = self.cursor.execute("SELECT * FROM Products;")
            # Running queries in our python program to access database and table inside DB
            for records in product_rows:
                # Iterate through the table data and list the unit prices
                print("Here are the unit prices available in the Products table:\n -> ")
                print(records.UnitPrice)
        else:
            return "Sorry, cannot fetch the data from this table, try again"
```
- Create Table method which prompts user to create table
```python
    def create_table(self):
        # Connect to database
        self.connect()
        action = input("Would you like to create a table? (Y/N)\n -> ").lower()
        if action == 'y':
            # Naming table and column names as well as the datatypes for the columns
            name = input("What would you like to name your table?\n -> ")
            columns = input("What two columns would you like to include?\n -> ").split()
            data_type = input("What data types would you like to assign to both columns?\n -> ").split()

            # Executing the create table comman which creates the table based on user input
            self.cursor.execute(f"CREATE TABLE {name} ({columns[0]} {data_type[0]}, {columns[1]} {data_type[1]})")
            # Below code is needed to commit changes to DB
            self.northwind_connection.commit()
            print(f"Well done!! You have created a table called {name} in the {self.database} Database")
        elif action == 'n':
            print("Thank you for using this program")
```
- Insert Data into the table prompts user first
do determine what data they want to insert under the columns
provided in the table
```python
    def input_data_to_table(self):
        self.connect()
        # Ensures we are inserting data into the relevant table
        what_table = input("What table would you like to insert data into?\n -> ")
        # Prompts user for what data they want to insert into the relevant columbs of the table
        what_data = input("What data would you like to insert into the columns?\n Format: Row1Value1, Row1Value2 Row2Value1 Row2Value2.. -> ").split()
        if what_table == 'Matt_table':
            # Executes the insert with all the relevant values inserted into the sql comman
            self.cursor.execute(f"""
                            INSERT INTO {self.database}.dbo.Matt_table (Name, Hobby)
                            VALUES
                            ('{what_data[0]}', '{what_data[1]}'),
                            ('{what_data[2]}', '{what_data[3]}')
                                """)
            # Commits the changes to the table
            self.northwind_connection.commit()
            print("Well done!! You have inserted your data into the relevant table")
        else:
            print("Sorry invalid table, choose the most suitable table")
```
- Check table method to display the table that was created
```python
    def check_table(self):
        # Function checks the table has been created and information added
        self.connect()
        test_table = self.cursor.execute("SELECT * FROM dbo.Matt_table")
        for records in test_table:
            # Prints records in the table
            print(records)
```

## Iteration 2 Task
**An sql manager for the products table**
- Create an object that relates only to the products table in 
the Northwind database. The reason for creating a single object 
for any table within the database would be to ensure that all 
functionality we build into this relates to what could be defined 
as a 'business function'.

- As an example the products table, although relating to the rest of 
the company, will service a particular area of the business in this 
scenario we will simply call them the 'stock' department.

- The stock department may have numerous requirements and it makes sense 
to contain all the requirements a code actions within a single object.

- Create two files nw_products.py & nw_runner.py and then we will move 
into creating our object.

**Our first requirement...**
- We've had a requirement for the stock department to print out the average 
value of all of our stock items.

Away we go....

**!!!Important Note!!! It would be more efficient to write the SQL query 
to find the data and compute the value and simply return the value in Python.**

### Solution
- The task focuses on writing a method which output the average price of the
units within the Products table
- First we make the class and connect to the database..
```python
import pyodbc

class SQL_Manager:
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"

    # Connect method so we can connect to the database
    def connect(self):
        self.northwind_connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        # Cursor is location of your mouse/current path
        self.cursor = self.northwind_connection.cursor()
```
- Once connection is set we can write the method to calculate the average
price of the products:
```python
    def unitprice_average(self):
        self.connect()
        # Empty list which we can add rows of data at each iteration
        average = []
        # Query to select the desired column to be iterated over i.e. unit price
        sql_query = "SELECT UnitPrice FROM Products;"
        # Runs the query and returns one row every time
        with self.cursor.execute(sql_query):
            one_row = self.cursor.fetchone()
            while one_row:
                # Once data from a row is appended into the average list, it goes to the next row
                average.append(int(one_row[0]))
                one_row = self.cursor.fetchone()
        # Returns the average by summing all the values and dividing by the amount
        return sum(average) / len(average)
```
- To run/test the method, we can call an instance and method in `def main()`
```python

def main():
    # Creating an instance of class to test functionality
    test = SQL_Manager()
    print(test.unitprice_average())

if __name__ == '__main__':
    main()
```