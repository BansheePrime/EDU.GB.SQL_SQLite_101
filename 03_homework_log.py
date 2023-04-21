#!/usr/bin/env python3
'''
Database should be in same directory and named as "teachers.db"
'''
import sqlite3

db_connection = sqlite3.connect("teachers.db")
cursor = db_connection.cursor()

columns_names = cursor.execute("SELECT * FROM streams_tb")
names = list(map(lambda i: i[0], columns_names.description))

print(f"Колонки таблицы streams_tb до переименования: ")
for name in names:
    print(name)

column_rename_query = '''ALTER TABLE streams_tb
                        RENAME COLUMN starting_date TO started_at;'''

column_add_query = '''ALTER TABLE streams_tb
                        ADD COLUMN finished_at TEXT;'''

# db_connection.commit()
db_connection.close()
