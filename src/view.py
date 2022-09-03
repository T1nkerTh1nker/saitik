import os
import json
from app import app
from flask import render_template, redirect


@app.route('/')
@app.route('/home')
def index():
    encode_projects = []
    project_dir = os.path.join(app.root_path, 'static', 'user_project')
    for project_file in os.listdir(project_dir):
        if os.path.isfile(os.path.join(project_dir, project_file)):
            encode_project = None
            with open(os.path.join(project_dir, project_file)) as file:
                encode_project = json.load(file)
            if encode_project is None:
                continue
            encode_projects.append(encode_project)

    return render_template('project_view.html', projects=encode_projects)
