import os

from flask import Flask, render_template, redirect, request, session
from flask_session import Session
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from functools import wraps
from festival_database.models import Act, Event, db
from datetime import datetime, timedelta

app = Flask(__name__)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("mainpage.html")


# @app.route("/festivals", methods=["GET", "POST"])
# def festivals():
#     if request.method == "POST":
#         return render_template("festivals.html")
#     elif request.method == "GET":
#         return redirect("/")

@app.route("/defqon1", methods=["GET", "POST"])
def defqon1():
    target_date = datetime.strptime("2023-06-23", "%Y-%m-%d").date()

    # Query acts that start on the specified date
    events = Act.query.filter(Act.start >= target_date, Act.start < target_date + timedelta(days=1)).all()

    return render_template("defqon1.html", events=events)
    


@app.route("/defqonfriday", methods=["GET", "POST"])
def defqonfriday():
    if request.method == "POST":
        return render_template("defqonfriday.html")
    elif request.method == "GET":
        return redirect("/")
        # connection = psycopg2.connect(
        #     host=DB_HOST,
        #     database=DB_NAME,
        #     user=DB_USER,
        #     password=DB_PASSWORD
        # )

        # cursor = connection.cursor()

        # cursor.execute("SELECT * FROM Defqon_1_2023_Timetable_friday")

        # friday_schedule = cursor.fetchall()

        # cursor.close()
        # connection.close()

        # return render_template('defqonfriday.html', friday_schedule=friday_schedule)



