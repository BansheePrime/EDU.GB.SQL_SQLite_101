#!/usr/bin/env python3
'''
Database should be in same directory and named as "teachers.db"
'''
import sqlite3
import re

db_connection = sqlite3.connect("teachers.db")
cursor = db_connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
records = cursor.fetchall()

cleaning_output = ('sqlite_sequence',)
records.remove(cleaning_output)

tables_names = []

for i in records:
    i = re.sub(r"^\(\'", "", str(i))
    i = re.sub(r"\'\,\)$", "", str(i))
    tables_names.append(i)

for j in tables_names:
    cursor.execute(f"SELECT * FROM {j}")
    table_content = cursor.fetchall()
    print(f"{j} contains following data: {table_content}")

db_connection.close()
