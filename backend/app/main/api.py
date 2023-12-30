from pprint import pprint
from flask import jsonify, make_response, request, render_template
from app import db
from app.main import bp
from app.analysis import main as analysis
from app.detection import main as detection
from app.models import User, Resource

@bp.route('/api-info', methods=["GET"])
def apiInfo():
    return jsonify('Api info!')

@bp.route('/api-traffic', methods=["GET"])
def apiDetectionTraffic():
    video_path = 'https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4'
    detector = detection.DetectionTraffic(video_path, time_seconds=5, contour=200)
    result = detector.detect_traffic()
    return jsonify(result)

@bp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found!'}), 404)
