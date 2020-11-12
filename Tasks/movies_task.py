import pyodbc
import pandas as pd

movies_csv = pd.read_csv(r'C:\Users\poiro\PycharmProjects\Python_with_SQL\Tasks\imdbtitles.csv')
data_frame = pd.DataFrame(movies_csv, columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult',
                                               'startYear', 'endYear', 'runtimeMinutes', 'genres'])


server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"

connect = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# Cursor is location of your mouse/current path
cursor = connect.cursor()


# Create a table for the data in SQL DB
cursor.execute("CREATE TABLE matt_movies_table (titleType VARCHAR(255), primaryTitle VARCHAR(255), "
               "originalTitle VARCHAR(255), isAdult INT, startYear INT, endYear VARCHAR(255), runtimeMinutes VARCHAR(255), genres VARCHAR(255")

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

