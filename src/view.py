import os
import json
from app import app
from src.projectparser import ProjectParser
from flask import render_template, redirect


@app.route('/')
@app.route('/home')
def index():
    projects = ProjectParser.get_project_name_description()
    artists = ProjectParser.get_artists()
    return render_template('project_view.html', projects=projects, artists=artists)
