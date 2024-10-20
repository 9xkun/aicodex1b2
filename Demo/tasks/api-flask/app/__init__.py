from flask import Flask
from app.users.user_blueprint import user_bp
from flask_migrate import Migrate
from app.database import db
from app.users.userweb_controller import UserWebController
from flask_cors import CORS

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
    CORS(app)
    # add swagger

    # create tables
    with app.app_context():
        db.create_all()

    app.register_blueprint(user_bp, url_prefix='/api')

    # TODO: support also with / or without

    # TODO: move to router
    @app.route('/users')
    def list_users():
        return UserWebController.list_users()
    
    return app