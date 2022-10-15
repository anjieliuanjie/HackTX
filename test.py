import pandas as pd
import numpy as np
import sqlite3
import pyodbc
from flask import Flask, render_template, send_file, make_response, url_for, Response, redirect, request
import os
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp
print("jasmine".capitalize())

url = "https://raw.githubusercontent.com/anjieliuanjie/HackTX/main/Data%20for%20repository.csv"
bolly = pd.read_csv(url)

# Capitalizing first character of genre title
bolly.Genre = bolly.Genre.str.capitalize()





#df = pd.DataFrame(bolly)
print(bolly[:10].to_string())
#bolly.info()
print(bolly.Genre.unique())
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("websiteTemplate.html",
                               genreOptions = bolly.Genre.unique())
    else:
        return "working on it"
