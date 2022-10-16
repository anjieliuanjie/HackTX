import pandas as pd
import numpy as np
import sqlite3
import pyodbc
from flask import Flask, render_template, send_file, make_response, url_for, Response, redirect, request
import os
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp

url = "https://raw.githubusercontent.com/anjieliuanjie/HackTX/main/Data%20for%20repository.csv"
bolly = pd.read_csv(url)

# Capitalizing first character of genre title, removing underscores
bolly.Genre = bolly.Genre.str.capitalize()
bolly.Genre.replace("Love_story", "Love story", inplace=True)
bolly.Genre.replace("Rom__com", "Rom-com", inplace=True)

# testing, can be deleted
print(bolly[:10].to_string())
print(bolly.Genre.unique())
# bolly.info()

# Rename column names
bolly.rename(columns={'Lead Star': 'LeadStar', 'Release Period': 'ReleasePeriod'}, inplace=True)

# Sort actor and director names
actors = bolly.LeadStar.unique()
actors.sort()

directors = bolly.Director.unique()
directors.sort()

# HTML
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("userInput.html",
                               periodOptions=bolly.ReleasePeriod.unique(),
                               genreOptions=bolly.Genre.unique(),
                               actorOptions=actors,
                               directorOptions=directors)
    else:
        print("testing")
        periodOpt = request.form.get("period")
        print(periodOpt)
        return render_template("userInput.html", periodOpt)
