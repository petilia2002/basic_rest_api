from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.db.models import db
from app.routes.postRoutes import post_bp
from app.routes.fileRoutes import file_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Enable CORS
    CORS(app)

    # Create database tables
    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(post_bp, url_prefix="/api")
    app.register_blueprint(file_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])
