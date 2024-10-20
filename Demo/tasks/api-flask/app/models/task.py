from datetime import datetime
from app.database import db

class Task(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    duedate = db.Column(db.DateTime, nullable=True)
    descript = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, name, duedate=None, descript=None, user_id=None):
        self.name = name
        self.duedate = duedate
        self.descript = descript
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'duedate': self.duedate,
            'descript': self.descript,
            'user_id': self.user_id
        }