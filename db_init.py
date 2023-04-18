#!/usr/bin/env python3
import sqlite3

db_connection = sqlite3.connect("teachers.db")
cursor = db_connection.cursor()

'''
teachers
courses
streams
grades
'''

