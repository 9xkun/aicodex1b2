from flask import Flask
from app.blueprints.user_blueprint import user_bp
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.database import db

migrate = Migrate()

# factory
# support injector
def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_bp, url_prefix='/api/users')

    with app.app_context():
        db.create_all()

    return app