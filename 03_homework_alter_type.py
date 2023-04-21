#!/usr/bin/env python3
'''
Database should be in same directory and named as "teachers.db"
'''
import sqlite3

source_db = "teachers.db"
db_connection = sqlite3.connect(source_db)
cursor = db_connection.cursor()

tb_grades_query = '''CREATE TABLE grades_alter_type_tb (
                        teacher_id INTEGER NOT NULL,
                        stream_id REAL NOT NULL,
                        grade REAL NOT NULL,
                        PRIMARY KEY(teacher_id, stream_id),
                        FOREIGN KEY (teacher_id) REFERENCES teachers_tb(id),
                        FOREIGN KEY (stream_id) REFERENCES streams_tb(id));'''

cursor.execute(tb_grades_query)

copy_grades_data_query = (f"INSERT INTO grades_alter_type_tb SELECT * FROM grades_tb;")
cursor.execute(copy_grades_data_query)

drop_old_grades_tb_query = (f"DROP TABLE grades_tb;")
cursor.execute(drop_old_grades_tb_query)

rename_altered_tb_query = (f"ALTER TABLE grades_alter_type_tb RENAME TO grades_tb;")
cursor.execute(rename_altered_tb_query)

   
db_connection.commit()
db_connection.close()
