#!/usr/bin/env python3
import sqlite3

db_connection = sqlite3.connect("teachers.db")
cursor = db_connection.cursor()
cursor.execute("SELECT * FROM teachers_tb")
records = cursor.fetchall()

for i in records:
    print(i)

db_connection.close()
