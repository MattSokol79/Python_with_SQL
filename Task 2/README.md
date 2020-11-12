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
- Then, we can import the data provided in a text
file e.g. csv file for movies into python using
the pandas module
```python
# Saving the movie file into a variable in a readme fashion
movies_csv = pd.read_csv(r'C:\Users\poiro\PycharmProjects\Python_with_SQL\Tasks\imdbtitles.csv')
data_frame = pd.DataFrame(movies_csv, columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult',
                                               'startYear', 'endYear', 'runtimeMinutes', 'genres'])
# Can now see the table in a python format
```
- In order to transfer the data into an SQL DB
and create table etc. we first need to connect to 
DB:
```python
# Connecting to SQL DB
server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "***"
password = "***"

connect = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# Cursor is location of your mouse/current path
cursor = connect.cursor()
```
- Once the connection has been established, we can
begin creating our table in SQL:
```python
# Create a table for the movie data in SQL DB
cursor.execute("CREATE TABLE matt_movies_table (titleType VARCHAR(255), primaryTitle VARCHAR(255), "
               "originalTitle VARCHAR(255), isAdult INT, startYear INT, endYear VARCHAR(255), runtimeMinutes VARCHAR(255), genres VARCHAR(255)")
```
- Then we will need to insert all of the data within
the table imported from the csv file into the newly
created table in SQL:
```python
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
```
- Finally, we can export data FROM SQL to Python and
back into a text file e.g. csv
- First we need to query/select the table we wish
to export from SQL:
```python
# EXPORTING/Moving data from DB to text files etc
exported_movie_data = pd.read_sql_query("""
                          SELECT * FROM matt_movies_table
                          """, connect) # connect is the connection to the database
```
- Now that we have the table stored in a python 
variable, we can export it into an external
text file e.g. csv:
```python
# We assign a dataframe to our table obtained from the SQL DB and export to csv
data_frame_2 = pd.DataFrame(exported_movie_data)
data_frame_2.to_csv(r'C:\Users\poiro\PycharmProjects\Python_with_SQL\Tasks\sql_to_csv_movies.csv')
```