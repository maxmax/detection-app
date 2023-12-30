from flask import Blueprint

bp = Blueprint('detection', __name__)

from detection.api import api_info, api_demo_function
