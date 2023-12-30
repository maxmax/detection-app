from flask import Blueprint

bp = Blueprint(
    'main',
    __name__,
    static_folder='../templates/',
    template_folder='../templates/'
    )

from app.main import api, view
