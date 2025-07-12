from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

projects = [
    {
        "id": 1,
        "name": "My First Website",
        "description": "A basic HTML and CSS project."
    },
    {
        "id": 2,
        "name": "Todo List App",
        "description": "A simple app to manage daily tasks."
    },
    {
        "id": 3,
        "name": "Quotes API",
        "description": "A RESTful API for managing inspirational quotes."
    }
]


#route for the home page
@app.route('/')
def home():
    return render_template("home.html")

#route for the project page
@app.route('/projects')
def show_projects():
    return render_template("projects.html", projects=projects)

@app.route('/project/<int:id>')
def show_project(id):
    for project in projects:
        if project["id"]==id:
            return render_template("project_detail.html",project=project)
    abort(404)