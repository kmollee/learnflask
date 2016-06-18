'''
init database
'''
import sqlite3


with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE posts(title TEXT, Description TEXT)""")
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
