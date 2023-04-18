#!/usr/bin/env bash
# Ограничение скрипта - названия таблиц должны совпадать с названиями ниже
sqlite3 ./teachers.db <<EOF
.tables
.schema teachers_tb
.schema cources_tb
.schema streams_tb
.schema grades_tb
EOF
