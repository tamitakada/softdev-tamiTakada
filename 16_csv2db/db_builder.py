#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Dec 2020 -- The Time of the Rona

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE='discobandit.db'

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

command = 'CREATE TABLE courses (name course, mark INTEGER KEY, id INTEGER KEY)'          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

with open('courses.csv', newline='') as csvfile: # reading courses.csv
    reader = csv.DictReader(csvfile)

    for row in reader:
        command = 'INSERT INTO courses VALUES (\"' + row['code'] + '\", ' + row['mark'] + ', ' + row['id'] + ');'
        c.execute(command)

command = 'CREATE TABLE students (name student, age INTEGER KEY, id INTEGER KEY)'          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)

with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        command = 'INSERT INTO students VALUES (\"' + row['name'] + '\", ' + row['age'] + ', ' + row['id'] + ');'
        c.execute(command)

#==========================================================

db.commit() #save changes
db.close()  #close database

# def csv_to_db(filename, headers):
