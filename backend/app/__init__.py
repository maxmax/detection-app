from flask import Flask
from flask_cors import CORS, cross_origin
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.analysis import bp as analysis_bp
    app.register_blueprint(analysis_bp)
    from app.detection import bp as detection_bp
    app.register_blueprint(detection_bp)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/main')
    CORS(app)

    return app


from app import models
#if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0')
