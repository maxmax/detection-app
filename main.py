from flask import Flask
from detection.api import bp as detection_bp

app = Flask(__name__)
app.register_blueprint(detection_bp, url_prefix='/detection')

if __name__ == '__main__':
    app.run(debug=True)
