import pyodbc
import pandas as pd


# Creating a class with different functionalities for extracting and importing data in csv, python and SQL
class Movies:
    def __init__(self):
        # Connecting to SQL DB
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"

        self.connect = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        # Cursor is location of your mouse/current path
        self.cursor = self.connect.cursor()

        # Saving the movie file into a variable in a readme fashion
        self.movies_csv = pd.read_csv(r'C:\Users\poiro\PycharmProjects\Python_with_SQL\Task 2\imdbtitles.csv')
        # Can see the table in a python format
        self.data_frame = pd.DataFrame(self.movies_csv,
                                       columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult',
                                                'startYear', 'endYear', 'runtimeMinutes', 'genres'])
        self.menu()


    def sql_to_csv(self):
        # EXPORTING/Moving data from DB to text files etc
        sql_query = input("Input your query\n -> ")
        name_of_file = input("What would you like to name your file?\n -> ")
        exported_movie_data = pd.read_sql_query(f'{sql_query}', self.connect) # connect is the connection to the database
        # We assign a dataframe to our table obtained from the SQL DB and export to csv
        data_frame_2 = pd.DataFrame(exported_movie_data)
        data_frame_2.to_csv(fr'C:\Users\poiro\PycharmProjects\Python_with_SQL\Task 2\{name_of_file}.csv')
        print(data_frame_2)

    def create_table_sql(self):
        # Method creates matt_movies_table with all the columns provided in the csv file
        self.cursor.execute("CREATE TABLE matt_movies_table (titleType VARCHAR(255), primaryTitle VARCHAR(255), "
               "originalTitle VARCHAR(255), isAdult INT, startYear INT, endYear VARCHAR(255), runtimeMinutes VARCHAR(255), genres VARCHAR(255))")

    def import_from_csv(self):
        # Inserts data into the SQL table with the use of pandas i.e. csv -> Python -> SQL Table
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
        # Can search the Table for a specific movie
        movie = input("What movie would you like to search for?\n -> ")
        query = pd.read_sql_query(f"""
                        SELECT * FROM matt_movies_table WHERE primaryTitle = '{movie}'
                        """, self.connect)

        df1 = pd.DataFrame(query)
        # Prints the table in python with all relevant results
        print(df1)

    def insert_movie(self):
        while True:
            # Allows user to insert data into the table already created
            you_sure = input("Are you sure you want to insert data?(Y/N) \n -> ").lower()
            if you_sure == 'y':
                titleType = input("What is the type of the movie?\n -> ")
                primaryTitle = input("What is the primary title of the movie?\n -> ")
                originalTitle = input("What is the original title of the movie?\n -> ")
                isAdult = input("Is the movie R rated?\n (Format: 1 = yes, 2 = no) -> ")
                startYear = input("What is initial year of the movie?\n -> ")
                endYear = input("What is the end year of the movie?\n -> ")
                runtimeMinutes = input("How long is the movie in minutes?\n -> ")
                genres = input("What is the genre of the movie?\n -> ")

                # SQL query to insert data based on inputs
                self.cursor.execute(f"""
                                    INSERT INTO matt_movies_table (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
                                    VALUES ('{titleType}', '{primaryTitle}', '{originalTitle}', '{isAdult}', '{startYear}', '{endYear}', '{runtimeMinutes}', '{genres}'
                                    """)

                self.connect.commit()
            elif you_sure == 'n':
                break

    # Displaying a menu of options/available methods for the user to see and choose from
    def menu(self):
        print("""
              DISPLAY
              1. Create table in SQL DB
              2. Import data into created SQL Table
              3. Search for specific movie in SQL Table
              4. Insert movie into SQL Table
              5. Move Data from SQL to text file i.e. csv file
              -> Please choose an option (1,2,3,4,5,6 or exit to stop)
              """)
        while True:
            # User must choose an option seen in the Display
            user_choice = input("What would you like to do?\n -> ").lower()
            if user_choice == '1':
                self.create_table_sql()
                print("You have successfully created a table in SQL!")
            elif user_choice == '2':
                self.import_from_csv()
                print("You have successfully inserted data into your table!")
            elif user_choice == '3':
                self.search_movie()
                print("I hope you found the movie you were looking for!")
            elif user_choice == '4':
                self.insert_movie()
                print("You have successfully inserted movie details into the table!")
            elif user_choice == '5':
                self.sql_to_csv()
                print("You have successfully transferred your data from SQL to a csv file!")
            elif user_choice == 'exit':
                break

def main():
    test = Movies()


if __name__ == '__main__':
    main()