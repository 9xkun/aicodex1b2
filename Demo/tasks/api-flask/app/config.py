# Configuration settings for the Flask application

import os

# Get the base directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SQLite database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for session management
    SECRET_KEY = 'your-secret-key'

    # Other configuration settings
    # ...