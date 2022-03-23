from crypt import methods
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def show_projects():
    return render_template("index.html")

@app.route("projects/<projects_id>")
def show_tasks(project_id):
    return render_template("project-tasks.html", project_id=project_id)

@app.route("/add/project", methods=['POST'])
def add_project():
    return "added"

@app.route("/add/task/<project_id>", methods=['POST'])
def add_project():
    return "task added"

app.run(debug=True, host="127.0.0.1", port=3000)