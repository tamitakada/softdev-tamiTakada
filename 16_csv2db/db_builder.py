#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Dec 2020 -- The Time of the Rona

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE='discobandit.db'

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

def csv_to_db(filename, table, headers):
    with open(filename, newline='') as csvfile: # reading courses.csv
        reader = csv.DictReader(csvfile)

        for row in reader:
            command = 'INSERT INTO ' + table + ' VALUES (\"'
            for i in range(len(headers)):
                command += row[headers[i]]
                if i == len(headers) - 1:
                    command += ');'
                elif i == 0:
                    command += '\", '
                else:
                    command += ', '
            # print(command)
            c.execute(command)

#==========================================================

command = 'CREATE TABLE courses (name course, mark INTEGER KEY, id INTEGER KEY)'          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

csv_to_db('courses.csv', 'courses', ['code', 'mark', 'id'])

command = 'CREATE TABLE students (name student, age INTEGER KEY, id INTEGER KEY)'          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)

csv_to_db('students.csv', 'students', ['name', 'age', 'id'])

#==========================================================

db.commit() #save changes
db.close()  #close database
