from flask import request, jsonify

from app.users.user_service import UserService
import re

from app.utils.validate_string import ValidateString


# transport
# transport_model: DTO, VO, flat data
class UserController:
    PHONE_LENGTH_VN = 10
    @staticmethod
    def create_user():
        # data = { 'firstname': 'John', 'lastname': 'Doe', 'email': 'jonh@mail.com', 'phone': '1234567890', 'age': 20 }
        data = request.get_json()

        # 1. validate email format (guard clause)
        email = data.get('email')
        if not email:
            return jsonify({'message': 'Email is required'}), 400
        
        if not ValidateString.validate_email_format(email):
            return jsonify({'message': 'Invalid email format'}), 400

        # 2. if have phone, validate phone length
        # eg, phone = 1234567890 -> ok
        # eg, phone = 123456789012 -> not ok
        # eg, phone = 123456789 -> not ok
        phone = data.get('phone')
        if phone and len(phone) != UserController.PHONE_LENGTH_VN:
            return jsonify({'message': 'Phone should be 10 digits'}), 400

        # 3. firstname and lastname should be < 50 characters
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        if (firstname and len(firstname) > 50) or (lastname and len(lastname) > 50):
            return jsonify({'message': 'Firstname and lastname should be less than 50 characters'}), 400

        # 4. age should be between 0 and 100
        age = data.get('age')
        ageInt = int(age)
        if ageInt and (ageInt < 0 or ageInt > 100):
            return jsonify({'message': 'Age should be between 0 and 100'}), 400
        
        # 5. validate password length >= 6
        password = data.get('password')
        if password is None or len(password) < 6:
            return jsonify({'message': 'Password should be at least 6 characters'}), 400

        if False:
            return jsonify({'message': 'Error'}), 500

        try:
            user = UserService.create_user(data)
        except Exception as e:
            return jsonify({'message': str(e)}), 500

        return jsonify(user.to_dict()), 201

    @staticmethod
    def get_user(user_id):
        user = UserService.get_user_by_id(user_id)
        if user:
            return jsonify(user.to_dict()), 200
        return jsonify({'message': 'User not found'}), 404

    @staticmethod
    def update_user(user_id):
        data = request.get_json()
        user = UserService.update_user(user_id, data)
        if user:
            return jsonify(user.to_dict()), 200
        return jsonify({'message': 'User not found'}), 404

    @staticmethod
    def delete_user(user_id):
        success = UserService.delete_user(user_id)
        if success:
            return jsonify({'message': 'User deleted'}), 204
        return jsonify({'message': 'User not found'}), 404
    
    @staticmethod
    def get_users():
        users = UserService.get_all_users()
        users_list = []
        for user in users:
            users_list.append(user.to_dict())
        return jsonify(users_list), 200