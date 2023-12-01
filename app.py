import os

from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from functools import wraps

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("mainpage.html")


@app.route("/festivals", methods=["GET", "POST"])
def festivals():
    if request.method == "POST":
        return render_template("festivals.html")
    elif request.method == "GET":
        return redirect("/")

