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

    def check_table(self):
        # Function checks the table has been created and information added
        self.connect()
        test_table = self.cursor.execute("SELECT * FROM dbo.Matt_table")
        for records in test_table:
            # Prints records in the table
            print(records)


def main():
    test = Pyodbc_Connection()
    #test.create_table()
    #test.input_data_to_table()
    test.check_table()
    #test.get_UnitPrice()

if __name__ == '__main__':
    main()


