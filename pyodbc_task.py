import pyodbc

class Pyodbc_Connection:
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "*****"
        self.password = "*****"


    def connect(self):
        self.northwind_connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        # Cursor is location of your mouse/current path
        self.cursor = self.northwind_connection.cursor()

    def get_UnitPrice(self):
        self.connect()
        what_table = input("What table would you like to use?\n -> ").title()
        if what_table == 'Products':
            product_rows = self.cursor.execute("SELECT * FROM Products;")
            # Running queries in our python program to access database and table inside DB
            for records in product_rows:
                # Iterate through the table data and list the unit prices
                print(records.UnitPrice)
        else:
            return "Sorry, cannot fetch the data from this table, try again"

    def create_table(self):
        self.connect()
        action = input("Would you like to create a table? (Y/N)\n -> ").lower()
        if action == 'y':
            name = input("What would you like to name your table?\n -> ")
            columns = input("What two columns would you like to include?\n -> ").split()
            data_type = input("What data type would you like to assign to both columns?\n -> ").split()

            self.cursor.execute(f"CREATE TABLE {name} ({columns[0]} {data_type[0]}, {columns[1]} {data_type[1]})")
            print(f"Well done!! You have created a table called {name} in the {self.database}")
        elif action == 'n':
            print("Thank you for using this program")

    def input_data_to_table(self):
        self.connect()
        what_table = input("What table would you like to insert data into?\n -> ")
        what_data = input("What data would you like to insert into the columns?\n Format: Row1Value1, Row1Value2 Row2Value1 Row2Value2.. -> ").split()
        if what_table == 'Matt_table':
            self.cursor.execute(f"""
                            INSERT INTO {self.database}.dbo.Matt_table (Name, Hobby)
                            VALUES
                            ({what_data[0]}, {what_data[1]}),
                            ({what_data[2]}, {what_data[3]})
                                """)
            self.northwind_connection.commit()
            print("Well done!! You have inserted your data into the relevant table")
        else:
            print("Sorry invalid table, choose the most suitable table")

    def check_table(self):
        self.connect()
        test_table = self.cursor.execute("SELECT * FROM Matt_table")
        for records in test_table:
            print(records)


def main():
    test = Pyodbc_Connection()
    #test.create_table()

    test.check_table()

if __name__ == '__main__':
    main()


