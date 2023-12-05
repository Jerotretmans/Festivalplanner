import os

from flask import Flask, render_template, redirect, request, session
from flask_session import Session
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from functools import wraps

app = Flask(__name__)

DB_HOST = 'localhost'
DB_NAME = 'timetables'
DB_USER = 'jerotretmans'
DB_PASSWORD = 'Propercorn.2'

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("mainpage.html")


@app.route("/festivals", methods=["GET", "POST"])
def festivals():
    if request.method == "POST":
        return render_template("festivals.html")
    elif request.method == "GET":
        return redirect("/")

@app.route("/defqon1", methods=["GET", "POST"])
def defqon1():
    if request.method == "POST":
        return render_template("defqon1.html")
    elif request.method == "GET":
        return redirect("/")

@app.route("/defqonfriday", methods=["GET", "POST"])
def defqonfriday():
    if request.method == "POST":
        return render_template("defqonfriday.html")
    elif request.method == "GET":
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Defqon_1_2023_Timetable_friday")

        friday_schedule = cursor.fetchall()

        cursor.close()
        connection.close()

        return render_template('defqonfriday.html', friday_schedule=friday_schedule)



