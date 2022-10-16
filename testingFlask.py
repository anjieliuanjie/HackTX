import os
from flask import Flask, redirect, render_template, request
import mysql.connector

import sqlite3

from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp

app = Flask(__name__)

moviesdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='JAM2022HTX',
    port='3306',
    database='testingdb'
)
cursor = moviesdb.cursor()

genreList = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy',
             'History', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', ]

cursor.execute('SELECT Genre FROM imdbTable')
all_genres = cursor.fetchall()

cursor.execute('SELECT Director FROM imdbTable')
all_directors = cursor.fetchall()
director_list = []
for i in range(len(all_directors)):
    count = 0
    for j in range(len(all_directors)):
        if all_directors[j] == all_directors[i]:
            count += 1
    if count == 1:
        director_list.append(all_directors[i])

print(director_list)
@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        return 'working on it'
    else:
        return render_template("userInput.html", genres=genreList)
