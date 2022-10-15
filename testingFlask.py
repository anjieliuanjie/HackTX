import os
from flask import Flask, redirect, render_template, request

from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("websiteTemplate.html", message = "hi there")
    else:
        return "working on it"
