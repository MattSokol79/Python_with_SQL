import pyodbc
import pandas as pd


# Creating a class with different functionalities
class Table_Functionality:
    def __init__(self):
        # Connecting to SQL DB
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "*****"
        self.password = "*****"

        self.connect = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        # Cursor is location of your mouse/current path
        self.cursor = self.connect.cursor()

    def csv_to_python(self):
        # Saving the movie file into a variable in a readme fashion
        self.movies_csv = pd.read_csv(r'C:\Users\poiro\PycharmProjects\Python_with_SQL\Tasks\imdbtitles.csv')
        # Can see the table in a python format
        self.data_frame = pd.DataFrame(self.movies_csv, columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult',
                                                       'startYear', 'endYear', 'runtimeMinutes', 'genres'])

    def sql_to_csv(self):
        # EXPORTING/Moving data from DB to text files etc
        sql_query = input("Input your query\n -> ")
        name_of_file = input()
        exported_movie_data = pd.read_sql_query(f'{sql_query}', self.connect) # connect is the connection to the database
        # We assign a dataframe to our table obtained from the SQL DB and export to csv
        data_frame_2 = pd.DataFrame(exported_movie_data)
        data_frame_2.to_csv(r'C:\Users\poiro\PycharmProjects\Python_with_SQL\Tasks\sql_to_csv_movies.csv')

    def create_table_sql(self):
        self.cursor.execute("CREATE TABLE matt_movies_table ((titleType VARCHAR(255), primaryTitle VARCHAR(255), "
               "originalTitle VARCHAR(255), isAdult INT, startYear INT, endYear VARCHAR(255), runtimeMinutes VARCHAR(255), genres VARCHAR(255)")

    def import_from_csv(self):
        for row in self.data_frame.itertuples():
            self.cursor.execute("""
                            INSERT INTO matt_movies_table (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                           row.titleType,
                           row.primaryTitle,
                           row.originalTitle,
                           row.isAdult,
                           row.startYear,
                           row.endYear,
                           row.runtimeMinutes,
                           row.genres)
            self.connect.commit()

    def search_movie(self):
        movie = input("What movie would you like to search for?\n -> ")
        query = pd.read_sql_query(f"""
                        SELECT * FROM matt_movies_table WHERE primaryTitle = '{movie}'
                        """, self.connect)
        df1 = pd.DataFrame(query)
        return df1

    def insert_movie(self):
        you_sure = input("Are you sure you want to insert data?(Y/N) \n -> ").lower()

        while you_sure == 'y':
            titleType = input("What is the type of the movie?\n -> ")
            primaryTitle = input("What is the primary title of the movie?\n -> ")
            originalTitle = input("What is the original title of the movie?\n -> ")
            isAdult = input("Is the movie R rated?\n (Format: 1 = yes, 2 = no) -> ")
            startYear = input("What is initial year of the movie?\n -> ")
            endYear = input("What is the end year of the movie?\n -> ")
            runtimeMinutes = input("How long is the movie in minutes?\n -> ")
            genres = input("What is the genre of the movie?\n -> ")


            self.cursor.execute(f"""
                               INSERT INTO matt_movies_table (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
                               VALUES ('{titleType}', '{primaryTitle}', '{originalTitle}', '{isAdult}', '{startYear}', '{endYear}', '{runtimeMinutes}', '{genres}'
                                """)

            self.connect.commit()
