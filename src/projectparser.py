import json
import os

from app import app
from src.projectstruct import ProjectStruct


class ProjectParser:
    USER_DIRECTORY = os.path.join(app.root_path, 'static', 'user_project')
    PROJECTS_FILE = 'projects.json'
    ARTISTS_FILE = 'artists.json'

    @staticmethod
    def get_artists():
        artists_path = os.path.join(ProjectParser.USER_DIRECTORY, ProjectParser.ARTISTS_FILE)
        ret_artists = []
        if os.path.isfile(artists_path):
            with open(artists_path, 'r') as file:
                ret_artists = json.load(file)
        return ret_artists

    @staticmethod
    def add_artists(artists:list):
        if not isinstance(artists, (list, tuple)):
            raise ValueError('Unexpected type.')
        artists_path = os.path.join(ProjectParser.USER_DIRECTORY, ProjectParser.ARTISTS_FILE)
        old_artists = []
        if os.path.isfile(artists_path):
            with open(artists_path) as file:
                old_artists = json.load(file)
        old_artists.extend(artists)
        with open(artists_path, 'w') as file:
            json.dump(old_artists, file, indent=4)

    @staticmethod
    def get_project_name_description():
        projects_path = os.path.join(ProjectParser.USER_DIRECTORY, ProjectParser.PROJECTS_FILE)
        ret_projects = []
        if os.path.isfile(projects_path):
            with open(projects_path) as file:
                ret_projects = json.load(file)
            ret = []
            for project in ret_projects:
                ret.append(ProjectStruct(project['name'], project['description']))
        return ret_projects

    @staticmethod
    def get_projects():
        projects_path = os.path.join(ProjectParser.USER_DIRECTORY, ProjectParser.PROJECTS_FILE)
        ret_projects = []
        if os.path.isfile(projects_path):
            with open(projects_path) as file:
                ret_projects = json.load(file)
            ret = []
            for project in ret_projects:
                ret.append(ProjectStruct(**project))
        return ret_projects

    @staticmethod
    def add_projects(projects):
        if not isinstance(projects, (list, tuple, ProjectStruct)):
            raise ValueError('Unexpected type.')
        projects_path = os.path.join(ProjectParser.USER_DIRECTORY, ProjectParser.PROJECTS_FILE)
        old_projects = []
        if os.path.isfile(projects_path):
            with open(projects_path, 'r') as file:
                old_projects = json.load(file)
        if isinstance(projects, (tuple, list)):
            for project in projects:
                if not isinstance(project, ProjectStruct):
                    raise ValueError('Unexpected type')
                old_projects.append(project.to_dict())
        else:
            old_projects.append(projects.to_dict())
        with open(projects_path, 'w') as file:
            json.dump(old_projects, file, indent=4)
