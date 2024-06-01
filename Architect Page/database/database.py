import sqlite3

conn =  sqlite3.connect('architect.db')
cursor = conn.cursor()


# create table for images ( )
query = 'CREATE TABLE IF NOT EXISTS images(id INTEGER PRIMARY KEY NOT NULL, image TEXT NOT NULL)'
cursor.execute(query)

#add images
query = '''INSERT INTO images VALUES (1, "https://i.imgur.com/v9YSDnn.jpeg"),
(2, "https://i.imgur.com/aEtoU3E.jpeg"),
(3, "https://i.imgur.com/FLZuyNC.jpeg"),
(4, "https://i.imgur.com/avI1Q1O.jpeg"),
(5, "https://i.imgur.com/XxYxOOQ.png"),
(6, "https://i.imgur.com/CGZOd.jpeg"),
(7, "https://i.imgur.com/EeSppj0.gif"),
(8, "https://i.imgur.com/ht7Drzv.gif"),
(9, "https://i.imgur.com/kAo2LG8.gif"),
(10, "https://i.imgur.com/kAo2LG8.gif")
'''
cursor.execute(query)


#get all data
cursor.execute('SELECT * FROM  images')
data = cursor.fetchall()
print("data:", data)

conn.commit()