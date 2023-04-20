#!/usr/bin/env bash
# Ограничение скрипта - названия таблиц должны совпадать с названиями ниже
sqlite3 ./teachers.db ".databases"
table_1st=$(sqlite3 ./teachers.db ".tables" | awk '{ print $1 }')
table_2nd=$(sqlite3 ./teachers.db ".tables" | awk '{ print $2 }')
table_3rd=$(sqlite3 ./teachers.db ".tables" | awk '{ print $3 }')
table_4th=$(sqlite3 ./teachers.db ".tables" | awk '{ print $4 }')
sqlite3 ./teachers.db ".schema $table_1st"
sqlite3 ./teachers.db ".schema $table_2nd"
sqlite3 ./teachers.db ".schema $table_3rd"
sqlite3 ./teachers.db ".schema $table_4th"
