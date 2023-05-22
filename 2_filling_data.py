#!/usr/bin/env python3
'''
Database should be in same directory and named as "teachers.db"
'''
import sqlite3
import csv
from pathlib import Path

source_db = "teachers.db"
db_connection = sqlite3.connect(source_db)
cursor = db_connection.cursor()

data_directory = Path('./data_sources')
teachers_file = data_directory / 'teachers.csv'
courses_file = data_directory / 'courses.csv'
streams_file = data_directory / 'streams.csv'
grades_file = data_directory / 'grades.csv'


with open(teachers_file, "r") as teachers_data:
    teachers_csv = csv.reader(teachers_data, delimiter=",")
    next(teachers_csv, None)
    id = ""
    name = ""
    surname = ""
    email = ""

    for row in teachers_csv:
        for i in range(len(row)):
            id = row[0]
            name = row[1]
            surname = row[2]
            email = row[3]
        
        add_teachers_data_query = (f"INSERT INTO teachers_tb VALUES ('{id}', '{name}', '{surname}', '{email}');")
        cursor.execute(add_teachers_data_query)

with open(courses_file, "r") as courses_data:
    courses_csv = csv.reader(courses_data, delimiter=",")
    next(courses_csv, None)
    id = ""
    name = ""

    for row in courses_csv:
        for i in range(len(row)):
            id = row[0]
            name = row[1]
        
        add_courses_data_query = (f"INSERT INTO courses_tb VALUES ('{id}', '{name}');")
        cursor.execute(add_courses_data_query)

with open(streams_file, "r") as streams_data:
    streams_csv = csv.reader(streams_data, delimiter=",")
    next(streams_csv, None)
    id = ""
    course_id = ""
    stream_number = ""
    started_at = ""
    finished_at = ""
    students_number = ""

    for row in streams_csv:
        for i in range(len(row)):
            id = row[0]
            course_id = row[1]
            stream_number = row[2]
            started_at = row[3]
            finished_at = row[4]
            students_number = row[5]
        
        add_streams_data_query = (f"INSERT INTO streams_tb VALUES ('{id}', '{course_id}', '{stream_number}', '{started_at}', {finished_at}, '{students_number}');")
        cursor.execute(add_streams_data_query)

with open(grades_file, "r") as grades_data:
    grades_csv = csv.reader(grades_data, delimiter=",")
    next(grades_csv, None)
    teacher_id = ""
    stream_id = ""
    grade = ""

    for row in grades_csv:
        for i in range(len(row)):
            teacher_id = row[0]
            stream_id = row[1]
            grade = row[2]
        
        add_grades_data_query = (f"INSERT INTO grades_tb VALUES ('{teacher_id}', '{stream_id}', '{grade}');")
        cursor.execute(add_grades_data_query)
   
db_connection.commit()
db_connection.close()
