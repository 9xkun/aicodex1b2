from flask import render_template
from app.services.user_service import UserService

class UserWebController:
    @staticmethod
    def list_users():
        users = UserService.get_all_users()
        return render_template('user_list.html', users=users)