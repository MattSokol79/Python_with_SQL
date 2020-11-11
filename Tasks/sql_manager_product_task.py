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


def main():
    # Creating an instance of class to test functionality
    test = SQL_Manager()
    print(test.unitprice_average())
    #test.check_table()

if __name__ == '__main__':
    main()

