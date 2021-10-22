#CrocCatGin - Rayat Roy, Michelle Lo, Tami Takada
#SoftDev
#K16 - All About Database
#2021-10-20

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE='discobandit.db'

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

def csv_to_db(filename, table, headers):
    """ Reads from the csv file and inputs data into the specified table in the database.
        The headers define the different columns in the csv file, and the first column
        is assumed to be a string type. """
    with open(filename, newline='') as csvfile: # reading courses.csv
        reader = csv.DictReader(csvfile)

        for row in reader:
            command = 'INSERT INTO ' + table + ' VALUES (\"'
            for i in range(len(headers)):
                command += row[headers[i]] # adds values of each column
                if i == len(headers) - 1:
                    command += ');'
                elif i == 0: # closes quotation mark for string
                    command += '\", '
                else:
                    command += ', '
            # print(command)
            c.execute(command)

command = 'CREATE TABLE courses (name course, mark INTEGER KEY, id INTEGER KEY)' # adds courses table
c.execute(command)    # run SQL statement

csv_to_db('courses.csv', 'courses', ['code', 'mark', 'id'])

command = 'CREATE TABLE students (name student, age INTEGER KEY, id INTEGER KEY)' # adds students table
c.execute(command)

csv_to_db('students.csv', 'students', ['name', 'age', 'id'])

#==========================================================

db.commit() #save changes
db.close()  #close database
