from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('architect.db', check_same_thread=False)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

@app.route("/", methods = ["GET", "POST"])
def GalleryPage():
    cursor.execute("SELECT * FROM images")

    rows = cursor.fetchall()
    print(rows)

    return render_template('gallery.html', rows = rows)