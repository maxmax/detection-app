from pprint import pprint
from flask import jsonify, make_response, request, render_template
from app import db
from app.main import bp
from app.analysis import main as analysis
from app.models import User, Resource

@bp.route('/api-info', methods=["GET"])
def api_info():
    return jsonify('Api info!')

@bp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found!'}), 404)
