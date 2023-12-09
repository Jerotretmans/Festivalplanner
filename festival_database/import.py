import csv
import os

from flask import Flask, render_template, request
from models import *

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    with app.app_context():
        f = open("events.csv")
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            event = Event(name=name)
            db.session.add(event)
            print(f"Added event with name {name}.")
        db.session.commit()

def import_data():
    with app.app_context():
        f = open("new_defqon_2023_timetable.csv")
        reader = csv.reader(f, quotechar="'", skipinitialspace=True)
        for row in reader:
            stage, start, end, act, event_name = row
            print(f"Adding act with stage {stage}, start time {start}, end time {end}, and name {act}, and event {event_name}.")

            event = Event.query.filter_by(name=event_name).first()
            assert event is not None, f"Could not find event {event_name}"
            
            act = Act(stage=stage, start=start, end=end, event=event.id, act=act)
            db.session.add(act)
        db.session.commit()

if __name__ == "__main__":
    main()
    import_data()