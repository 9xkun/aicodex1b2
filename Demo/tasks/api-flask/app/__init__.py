from flask import Flask
from app.database import db
from app.blueprints.user_blueprint import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    app.register_blueprint(user_bp, url_prefix='/api/users')

    with app.app_context():
        db.create_all()

    return app