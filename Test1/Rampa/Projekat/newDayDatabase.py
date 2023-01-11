import sqlite3
import datetime

today = str(datetime.date.today())
filename = "archive/%s.db" % (today)

connection = sqlite3.connect(filename)
cursor = connection.cursor()

cursor.execute('''CREATE TABLE telefon(id int PRIMARY KEY, time text, number text)''')
cursor.execute('''CREATE TABLE internet(id int PRIMARY KEY, time text, username text, ip text)''')

connection.commit()
connection.close()
