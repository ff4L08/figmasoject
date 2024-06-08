import sqlite3

conn =  sqlite3.connect('questions.db')
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


query = 'CREATE TABLE IF NOT EXISTS projects(ID INTEGER PRIMARY KEY NOT NULL, title TEXT NOT NULL, image TEXT, description TEXT)'
cursor.execute(query)


query = '''INSERT INTO projects VALUES (1, "X Blueprint", "https://images.pexels.com/photos/4386157/pexels-photo-4386157.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."), 
(2, "Quantum Perspectives", "https://images.pexels.com/photos/4568137/pexels-photo-4568137.jpeg?auto=compress&cs=tinysrgb&w=800", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."), 
(3, "Cobalt Framework", "https://images.pexels.com/photos/1423035/pexels-photo-1423035.jpeg?auto=compress&cs=tinysrgb&w=800", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."), 
(4, "Eden Visions", "https://images.pexels.com/photos/1671030/pexels-photo-1671030.jpeg?auto=compress&cs=tinysrgb&w=800", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."), 
(5, "Sapphire Harmony", "https://images.pexels.com/photos/4606702/pexels-photo-4606702.jpeg?auto=compress&cs=tinysrgb&w=800", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."), 
(6, "Terra Evolution", "https://images.pexels.com/photos/4616604/pexels-photo-4616604.jpeg?auto=compress&cs=tinysrgb&w=800", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."), 
(7, "Infinity Impact", "https://images.pexels.com/photos/4885204/pexels-photo-4885204.jpeg?auto=compress&cs=tinysrgb&w=800", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."), 
(8, "Kinetic Blueprint", "https://images.pexels.com/photos/4397203/pexels-photo-4397203.jpeg?auto=compress&cs=tinysrgb&w=800", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.") ,
(9, "Auric Ascent", "https://images.pexels.com/photos/7109498/pexels-photo-7109498.jpeg?auto=compress&cs=tinysrgb&w=800", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."), 
(10, "Verge Vision", "https://images.pexels.com/photos/5688667/pexels-photo-5688667.jpeg?auto=compress&cs=tinysrgb&w=800", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."), 
(11, "Platinum Harmony", "https://images.pexels.com/photos/4923347/pexels-photo-4923347.jpeg?auto=compress&cs=tinysrgb&w=800", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."), 
(12, "Silent Symphony", "https://images.pexels.com/photos/5910332/pexels-photo-5910332.jpeg?auto=compress&cs=tinysrgb&w=800", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
'''
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS porjectImages (ID INTEGER PRIMARY KEY NOT NULL, image1 TEXT, image2 TEXT, image3 TEXT)'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (1, "https://images.pexels.com/photos/23733220/pexels-photo-23733220/free-photo-of-a-black-and-white-photo-of-a-person-walking-through-an-empty-building.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", "https://images.pexels.com/photos/19254459/pexels-photo-19254459/free-photo-of-elegant-couple-walking-on-the-pavement-in-city.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load", "https://images.pexels.com/photos/25242983/pexels-photo-25242983/free-photo-of-a-house-with-a-roof-and-a-tree-in-the-background.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load")'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (2, "https://images.pexels.com/photos/9220184/pexels-photo-9220184.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load", "https://images.pexels.com/photos/12824811/pexels-photo-12824811.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load", "https://images.pexels.com/photos/25211647/pexels-photo-25211647/free-photo-of-brunette-in-elegant-vest-and-white-blouse.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load")'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (3, "https://images.pexels.com/photos/7515368/pexels-photo-7515368.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load", "https://images.pexels.com/photos/25016474/pexels-photo-25016474/free-photo-of-a-person-riding-a-bike-on-a-road-with-palm-trees.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load", "https://images.pexels.com/photos/25396309/pexels-photo-25396309/free-photo-of-a-white-table-with-a-red-flower-on-it.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load")'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (4,  "https://images.pexels.com/photos/25182696/pexels-photo-25182696/free-photo-of-a-cup-of-coffee-and-an-open-book-on-a-white-table.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load", "https://images.pexels.com/photos/16676371/pexels-photo-16676371/free-photo-of-dogs-sitting-on-beach.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load", "https://images.pexels.com/photos/18983112/pexels-photo-18983112/free-photo-of-table-after-breakfast-full-of-fruits.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load")'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (5,  "https://images.pexels.com/photos/20526734/pexels-photo-20526734/free-photo-of-white-monumental-colonnade.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load", "https://images.pexels.com/photos/12833697/pexels-photo-12833697.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load", "https://images.pexels.com/photos/20157706/pexels-photo-20157706/free-photo-of-tram-on-street-by-estrela-basilica-in-lisbon-portugal.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load")'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (6,  "https://images.pexels.com/photos/25396259/pexels-photo-25396259/free-photo-of-a-silver-tray-with-knives-and-forks-on-it.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load", "https://images.pexels.com/photos/20875307/pexels-photo-20875307/free-photo-of-a-car-driving-down-a-mountain-road-in-the-fall.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load", "https://images.pexels.com/photos/10404290/pexels-photo-10404290.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (7,  "", "", "")'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (8,  "", "", "")'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (9,  "", "", "")'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (10,  "", "", "")'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (11,  "", "", "")'
cursor.execute(query)

query = 'INSERT INTO porjectImages VALUES (12, "", "", "")'
cursor.execute(query)

conn.commit()