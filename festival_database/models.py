from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Act(db.Model):
    __tablename__ = "timetables"
    id = db.Column(db.Integer, primary_key =True)
    stage = db.Column(db.String, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    act = db.Column(db.String, nullable=False)
    event = db.Column("event", db.ForeignKey(Event.id), primary_key=False)
    

