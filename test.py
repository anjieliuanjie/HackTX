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
# df = pd.DataFrame(bolly)
bolly.rename(columns={'Lead Star': 'LeadStar', 'Release Period' : 'ReleasePeriod'}, inplace=True)
#print(bolly[:10].to_string())
bolly.info()
# print(bolly.Genre.unique())


actors = bolly.LeadStar.unique()
actors.sort()

directors = bolly.Director.unique()
directors.sort()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("websiteTemplate.html",
                               periodOptions=bolly.ReleasePeriod.unique(),
                               genreOptions=bolly.Genre.unique(),
                               actorOptions=actors,
                               directorOptions=directors)
    else:
        return "working on it"
