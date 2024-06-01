from flask import Flask, render_template, request, redirect, url_for
import math
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('architect.db', check_same_thread=False)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

currentPage = 1
max = 1

@app.route("/gallery/<currentPage>", methods = ["GET", "POST"])
def GalleryPage(currentPage=1):
    global max
    startIn = (int(currentPage)-1)*2+int(currentPage)
    endIn = int(currentPage)*3
    cursor.execute("SELECT * FROM images WHERE id between " + str(startIn) + " AND " + str(endIn))
    rows = cursor.fetchall()
    print(rows)

    query = "SELECT * FROM images"
    cursor.execute(query)
    data = cursor.fetchall()
    max = math.ceil(len(data)/3)

    return render_template('gallery.html', rows = rows, currentPage=currentPage, max = max) 


@app.route("/gallery/change/<action>", methods = ["GET", "POST"])
def changePage(action):
    global currentPage
    global max
    if action == "INC":
        if currentPage + 1 <= max:
            currentPage += 1
    elif currentPage - 1 > 0:
        currentPage -= 1
    return redirect(url_for('GalleryPage', currentPage=currentPage))

@app.route("/contacts/", methods = ["GET", "POST"])
def contactPage():
    return render_template('contact.html') 