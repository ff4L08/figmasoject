from flask import Flask, render_template, request, redirect,url_for
import sqlite3
import math

app = Flask(__name__)
conn = sqlite3.connect('questions.db', check_same_thread=False)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

currentPage = 1
max = 1

@app.route("/")
def Homescreen():
    return render_template('HomePage.html')


@app.route("/project/<currentPage>", methods =['GET', 'POST'])
def OurProjects(currentPage=1):
    global max

    startIn = ((int(currentPage)-1)*2)+int(currentPage)
    endIn = int(currentPage)*3

    query = "SELECT * FROM projects"
    cursor.execute(query)
    data = cursor.fetchall()
    max = math.ceil(len(data)/3)

    cursor.execute("SELECT * FROM projects WHERE ID BETWEEN " + str(startIn) + " AND " + str(endIn))


    rows = cursor.fetchall()

    return render_template('ourProjects.html', rows = rows, currentPage = currentPage, max = max)

@app.route("/project/change/<action>", methods =['GET', 'POST'])
def changePageOurProjects(action):
    global currentPage
    global max
    if action == "INC":
        if currentPage + 1 <= max:
            currentPage += 1
    else:
        if currentPage - 1 > 0:
            currentPage -= 1
    return redirect(url_for('OurProjects', currentPage=currentPage))

@app.route("/projectdetail<id>/")
def ProjectDetailPage(id):

    query = "SELECT * FROM porjectImages WHERE id == " + id
    cursor.execute(query)
    images = cursor.fetchall()
    query = "SELECT * FROM projects WHERE id == " + id
    cursor.execute(query)
    projects = cursor.fetchall()

    print(projects[0].description)

    return render_template('Project1.html', images = images[0], projects = projects[0]) 

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


@app.route("/gallery/change/<action>")
def changePageGalleryPage(action):
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

app.run('0.0.0.0')