from multiprocessing.sharedctypes import Value
from flask import Flask,render_template, request, jsonify
from p4_sumanth.task_model import TaskModel
from database.db import get_session
from sqlalchemy import Boolean, CHAR, Column, DateTime, Enum, Integer, String, Table, text
from sqlalchemy.ext.declarative import declarative_base

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'POSTGRES_LINK'


db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(Integer, primary_key=True, server_default=text("nextval('task_id_seq'::regclass)"))
    title = db.Column(String(30), nullable=False)
    description = db.Column(String(200), nullable=False)
    due_datetime = db.Column(DateTime, nullable=False)
    email = db.Column(String(254), nullable=False)
    color = db.Column(CHAR(6), nullable=False)
    priority = db.Column(Enum('low', 'medium', 'high', name='priority_t'), nullable=False)
    is_completed = db.Column(Boolean, nullable=False)

    def __init__(self,title,description,date,email,color,priority,completed):
        self.title = title
        self.description = description
        self.due_datetime = date
        self.email = email
        self.color = color
        self.priority = priority
        self.is_completed = completed



@app.route("/")
def home_page():
    return "<p> Home Page </p>"


@app.route("/get-task",methods=['GET'])
def get_task():
    #Application logic
    result = Task.query.get(1)

    #Validate response
    try:
        task_pydantic = TaskModel.from_orm(result)
    except ValueError:
        return "<p> Error occurred </p>"
    

    #Return response
    return jsonify(task_pydantic.dict())


if __name__ == "__main__":
    app.run()
