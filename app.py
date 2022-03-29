from flask import Flask, render_template

from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgre://postgree:password@localhost:5432/project_tracker')


app = Flask(__name__)

@app.route("/")
def show_projects():
    return render_template("index.html")

@app.route("/projects/<projects_id>")
def show_tasks(project_id):
    return render_template("project-tasks.html", project_id=project_id)

@app.route("/add/project", methods=['POST'])
def add_project():
    return "added"

@app.route("/add/task/<project_id>", methods=['POST'])
def add_task():
    return "task added"

app.run(debug=True, host="127.0.0.1", port=3000)