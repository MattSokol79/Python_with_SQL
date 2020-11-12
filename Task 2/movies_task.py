import pyodbc
import pandas as pd

# Saving the movie file into a variable in a readme fashion
movies_csv = pd.read_csv(r'C:\Users\poiro\PycharmProjects\Python_with_SQL\Tasks\imdbtitles.csv')
data_frame = pd.DataFrame(movies_csv, columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult',
                                               'startYear', 'endYear', 'runtimeMinutes', 'genres'])
# Can see the table in a python format
# Connecting to SQL DB
server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "*****"
password = "*****"

connect = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# Cursor is location of your mouse/current path
cursor = connect.cursor()




# Create a table for the movie data in SQL DB
cursor.execute("CREATE TABLE matt_movies_table (titleType VARCHAR(255), primaryTitle VARCHAR(255), "
               "originalTitle VARCHAR(255), isAdult INT, startYear INT, endYear VARCHAR(255), runtimeMinutes VARCHAR(255), genres VARCHAR(255)")

# Inserts all the relevant values row by row into the newly created table in SQL DB
for row in data_frame.itertuples():
    cursor.execute("""
                    INSERT INTO matt_movies_table (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                            row. titleType,
                            row.primaryTitle,
                            row.originalTitle,
                            row.isAdult,
                            row.startYear,
                            row.endYear,
                            row.runtimeMinutes,
                            row.genres)
    connect.commit()

# EXPORTING/Moving data from DB to text files etc
exported_movie_data = pd.read_sql_query("""
                          SELECT * FROM matt_movies_table
                          """, connect) # connect is the connection to the database

# We assign a dataframe to our table obtained from the SQL DB and export to csv
data_frame_2 = pd.DataFrame(exported_movie_data)
data_frame_2.to_csv(r'C:\Users\poiro\PycharmProjects\Python_with_SQL\Tasks\sql_to_csv_movies.csv')
