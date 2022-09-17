from flask import render_template, request, Flask
from run import responseTemplate, PATH_API
from blueprints.blueprint_user.blueprint_user import blueprint_user
from blueprints.blueprint_utilities.blueprint_utilities import blueprint_utilities
from blueprints.blueprint_api.api_places.api_places import api_places