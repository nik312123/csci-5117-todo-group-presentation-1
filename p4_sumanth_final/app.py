from datetime import datetime

import pydantic
from flask import Flask, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, CHAR, DateTime, Enum, Integer, String, text

from p4_sumanth_final.task_model import TaskModel

"""
If you want to try with data from an actual Postgres database, then create the database, run schema.sql,
add an entry in the task table with id of 1, change the postgres_link variable to the link to your database,
change actual_db to True, and run this script.
"""

actual_db = False
postgres_link = "POSTGRES_LINK"

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if actual_db:
    app.config['SQLALCHEMY_DATABASE_URI'] = postgres_link

db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = "task"
    
    id = db.Column(Integer, primary_key = True, server_default = text("nextval('task_id_seq'::regclass)"))
    title = db.Column(String(30), nullable = False)
    description = db.Column(String(200), nullable = False)
    due_datetime = db.Column(DateTime, nullable = False)
    email = db.Column(String(254), nullable = False)
    color = db.Column(CHAR(6), nullable = False)
    priority = db.Column(Enum("low", "medium", "high", name = "priority_t"), nullable = False)
    is_completed = db.Column(Boolean, nullable = False)
    
    def __init__(self, task_id, title, description, date, email, color, priority, completed):
        self.id = task_id
        self.title = title
        self.description = description
        self.due_datetime = date
        self.email = email
        self.color = color
        self.priority = priority
        self.is_completed = completed


@app.route("/")
def home_page():
    return f'<a href="{url_for("get_task")}">Click here to get a task example.</a>'


@app.route("/get-task", methods = ['GET'])
def get_task():
    # Application logic
    if actual_db:
        result = Task.query.get(1)
    else:
        result = Task(
            1,
            "Hello Goodbye 7 l33t",
            "This task is obviously about hello goodbye 7 l33t. What more do you need?",
            datetime(2022, 3, 31, 11, 32, 10),
            "chawl025@umn.edu",
            "0197F6",
            "low",
            False
        )
    
    # Validate response
    try:
        task_pydantic = TaskModel.from_orm(result)
    except pydantic.ValidationError as e:
        return f"<p>Error occurred: {str(e)}</p>"
    
    # Return response
    return Response(
        response = task_pydantic.json(by_alias = True),
        status = 200,
        mimetype = "application/json"
    )


if __name__ == "__main__":
    app.run()
