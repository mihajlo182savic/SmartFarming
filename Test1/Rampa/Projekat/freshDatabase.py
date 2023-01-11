import sqlite3

connection = sqlite3.connect('baza.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE korisnici (ime text, prezime text, username text PRIMARY KEY, password text)''')
cursor.execute('''CREATE TABLE admini (ime text, prezime text, username text PRIMARY KEY, password text)''')
cursor.execute('''CREATE TABLE telefoni (broj text PRIMARY KEY, username text)''')

connection.commit()
connection.close()
