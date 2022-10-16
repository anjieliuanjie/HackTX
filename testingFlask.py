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

cursor.execute('SELECT Director FROM imdbTable')
directors = cursor.fetchall()

for director in directors:
    print(director)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("userInput.html", message = "hi there")
    else:
        return "working on it"
