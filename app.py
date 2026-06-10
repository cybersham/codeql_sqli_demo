import sqlite3
import sys

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

user_input = sys.argv[1]

query = "SELECT * FROM users WHERE username = '" + user_input + "'"

cursor.execute(query)