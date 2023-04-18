#!/usr/bin/env python3
import sqlite3

my_connection = sqlite3.connect("gb_edu.db")
cursor = my_connection.cursor()

data = [
	{
		country: "South Africa",
		currency: "Rand",
		list: "13"
	},
	{
		country: "Italy",
		currency: "Euro",
		list: "3"
	},
	{
		country: "Pakistan",
		currency: "Rupee",
		list: "11"
	},
	{
		country: "Switzerland",
		currency: "Franc",
		list: "9"
	},
	{
		country: "South Korea",
		currency: "Won",
		list: "19"
	}
]

my_connection.close()
