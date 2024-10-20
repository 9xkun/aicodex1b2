from flask import Blueprint
from app.users.user_controller import UserController

user_bp = Blueprint('user_api', __name__)

user_bp.route('/users', methods=['GET'])(UserController.get_users)
user_bp.route('/users', methods=['POST'])(UserController.create_user)
user_bp.route('/users/<int:user_id>', methods=['GET'])(UserController.get_user)
user_bp.route('/users/<int:user_id>', methods=['PUT'])(UserController.update_user)
user_bp.route('/users/<int:user_id>', methods=['DELETE'])(UserController.delete_user)