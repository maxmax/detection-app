from flask import jsonify, render_template
from . import bp
from .functions import demo_detection, generate_frames, socketio

@bp.route('/api', methods=["GET"])
def api_info():
    return jsonify('Api info!')

@bp.route('/api-demo-detection', methods=["GET"])
def api_demo_function():
    result = demo_detection()
    return jsonify(result)
