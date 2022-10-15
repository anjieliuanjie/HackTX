import pandas as pd
import numpy as np
import sqlite3
import pyodbc
from flask import Flask, render_template, send_file, make_response, url_for, Response, redirect, request
import os
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp

url = "https://raw.githubusercontent.com/anjieliuanjie/HackTX/main/netflix_titles.csv"
netflix = pd.read_csv(url)
df = pd.DataFrame(netflix)


#print(netflix[:10].to_string())
#netflix.info()

a = netflix.type.unique()
print(a)



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("websiteTemplate.html", typeOptions = netflix.type.unique())
    else:
        return "working on it"
