__author__ = 'mkaplenko'
from flask import Blueprint


brpr_plugins = Blueprint('plugins', __name__, template_folder='templates', static_folder='static', url_prefix='/plugins')
