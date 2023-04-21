#!/usr/bin/env python3
'''
Database should be in same directory and named as "teachers.db"
'''
import sqlite3

source_db = "teachers.db"
source_table = "streams_tb"

db_connection = sqlite3.connect(source_db)
cursor = db_connection.cursor()

def show_columns():
    columns_names = cursor.execute(f"SELECT * FROM {source_table}")
    names = list(map(lambda i: i[0], columns_names.description))
    return print(' '.join(names))

print("Колонки таблицы streams_tb до переименования: ")
show_columns()

column_rename_query = '''ALTER TABLE streams_tb
                        RENAME COLUMN starting_date TO started_at;'''

cursor.execute(column_rename_query)
print("Колонки таблицы streams_tb после переименования: ")
show_columns()

column_add_query = '''ALTER TABLE streams_tb
                        ADD COLUMN finished_at TEXT;'''

cursor.execute(column_add_query)
print("Колонки таблицы streams_tb после добавления: ")
show_columns()

db_connection.commit()
db_connection.close()
