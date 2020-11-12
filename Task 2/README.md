# Task - SQL Movies CRUD
**Timings**
- 60 Minutes

**Summary**
- Now that you've learned how to connect to the DB using pyodbc you can start abstracting out interaction the db! This is great if you don't like writing sql.

**Tasks**
- CRUD the DB in python

Hint: create abstraction and methods to deal with db so you don't have too

**Acceptance Criteria**
- You can get all the movies
- You can search based on title
- You can add movies to DB

## Second iteration:

### IMDB CSV <> Py <> SQL
**Summary**
- You know how to parse txt files into python.
- You also know how to connect python into the db.
- You also know how to manipulated and change data with python.

Your task is to move data from text files into the db and from the the db into text files

**Tasks**
- Read the text file and create object
- Save object in DB
- Load that from DB and create object
- Output object to text file

**Extra:**
- Explore other APIs

**Acceptance Criteria**
- Able to take in 10 film names in text file and save to db
- Able to load data from DB and create text file with names

## Solution
- First we need to import the modules which will
allow us to import data from text files like csv
as well as connect to our SQL database:
```python
import pyodbc
import pandas as pd
```
- Then we can do many things, I created a Movies class which has 
different functionalities
- When the class is initialised, the connection to SQL is established
and menu pops up for the user to read from
```python

# Creating a class with different functionalities for extracting and importing data in csv, python and SQL
class Movies:
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

        self.menu()
```
- Menu provides user with different options they can choose from
and prompts them to select an action
```python
    # Displaying a menu of options/available methods for the user to see and choose from
    def menu(self):
        print("""
              DISPLAY
              1. Extract data from csv file to python
              2. Create table in SQL DB
              3. Import data into created SQL Table
              4. Search for specific movie in SQL Table
              5. Insert movie into SQL Table
              6. Move Data from SQL to text file i.e. csv file
              -> Please choose an option (1,2,3,4,5,6 or exit to stop)
              """)
        while True:
            # User must choose an option seen in the Display
            user_choice = input("What would you like to do?\n -> ").lower()
            if user_choice == '1':
                self.csv_to_python()
            elif user_choice == '2':
                self.create_table_sql()
            elif user_choice == '3':
                self.import_from_csv()
            elif user_choice == '4':
                self.search_movie()
            elif user_choice == '5':
                self.insert_movie()
            elif user_choice == '6':
                self.sql_to_csv()
            elif user_choice == 'exit':
                break
```
- The first method they can choose from (and should) is extracting
data from a text file csv to python
```python

    def csv_to_python(self):
        # Saving the movie file into a variable in a readme fashion
        self.movies_csv = pd.read_csv(r'C:\Users\poiro\PycharmProjects\Python_with_SQL\Task 2\imdbtitles.csv')
        # Can see the table in a python format
        self.data_frame = pd.DataFrame(self.movies_csv, columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult',
                                                       'startYear', 'endYear', 'runtimeMinutes', 'genres'])
```
- Once the data is stored within a variable in python, we can create a table
in SQL DB to store the data, i.e. option 2
```python
    def create_table_sql(self):
        # Method creates matt_movies_table with all the columns provided in the csv file
        self.cursor.execute("CREATE TABLE matt_movies_table ((titleType VARCHAR(255), primaryTitle VARCHAR(255), "
               "originalTitle VARCHAR(255), isAdult INT, startYear INT, endYear VARCHAR(255), runtimeMinutes VARCHAR(255), genres VARCHAR(255)")
```
- Option 3 inserts all of the extracted data obtained from the text file into
the SQL table named matt_movies_table
```python
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
```
- Now that we have the data in SQL DB, we can perform different queries
such as search for movies:
```python
    def search_movie(self):
        # Can search the Table for a specific movie
        movie = input("What movie would you like to search for?\n -> ")
        query = pd.read_sql_query(f"""
                        SELECT * FROM matt_movies_table WHERE primaryTitle = '{movie}'
                        """, self.connect)

        df1 = pd.DataFrame(query)
        # Prints the table in python with all relevant results
        print(df1)
```
- Or insert additional movie data:
```python
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
```
- The final option allows the user to extract their data from an SQL table
to python and into a csv/text file if they wish:
```python
    def sql_to_csv(self):
        # EXPORTING/Moving data from DB to text files etc
        sql_query = input("Input your query\n -> ")
        name_of_file = input("What would you like to name your file?\n -> ")
        exported_movie_data = pd.read_sql_query(f'{sql_query}', self.connect) # connect is the connection to the database
        # We assign a dataframe to our table obtained from the SQL DB and export to csv
        data_frame_2 = pd.DataFrame(exported_movie_data)
        data_frame_2.to_csv(fr'C:\Users\poiro\PycharmProjects\Python_with_SQL\Task_2\{name_of_file}.csv')
        print(data_frame_2)
```
- Finally, in order to run the program, an object of the class has to be 
created:
```python
def main():
    test = Movies()


if __name__ == '__main__':
    main()
```