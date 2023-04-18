#!/usr/bin/env python3
'''
teachers
courses
streams
grades
'''

import sqlite3
# import csv

db_connection = sqlite3.connect("teachers.db")
cursor = db_connection.cursor()
tables_list = []

tb_teachers_query = '''CREATE TABLE teachers_tb (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        surname TEXT NOT NULL,
                        email TEXT NOT NULL,
                        );'''


tb_courses_query = '''CREATE TABLE cources_tb (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE,
                        );'''

tb_streams_query = '''CREATE TABLE streams_tb (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        course_id INTEGER NOT NULL,
                        stream_number INTEGER NOT NULL UNIQUE,
                        starting_date TEXT NOT NULL,
                        students_number INTEGER NOT NULL,
                        FOREIGN KEY (course_id) REFERENCES courses_tb(id)
                        );'''

tb_grades_query = '''CREATE TABLE grades (
                        teacher_id INTEGER NOT NULL,
                        stream_id INTEGER NOT NULL,
                        grade REAL NOT NULL,
                        PRIMARY KEY(teacher_id, stream_id),
                        FOREIGN KEY (teacher_id) REFERENCES teachers_tb(id),
                        FOREIGN KEY (stream_id) REFERENCES streams_tb(id)
                        );'''


cursor.executemany(tables_list)

db_connection.close()

# if __name__ == '__main__':
#     main()
