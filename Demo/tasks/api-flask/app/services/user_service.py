from app.repositories.user_repository import UserRepository
from app.models.user import User
import logging

# business logic
# smart: accept nested data, business entity
# aggregate
class UserService:
    @staticmethod
    def create_user(data):
        user = User(**data)

        #1. validate email uniqueness
        userExisted = UserRepository.get_user_by_email(user.email)
        if userExisted:
            # log context (email exist in db, user contains email)
            logging.error(f"Create User: email {user.email} user_id {userExisted.id}")
            raise ValueError('Email already exists')
        
        #2. create user
        user = UserRepository.create_user(user)

        #3. send email to user to notify that user is created

        #4. sync with firebase repo


        return user

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            for key, value in data.items():
                setattr(user, key, value)
            return UserRepository.update_user(user)
        return None

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            UserRepository.delete_user(user)
            return True
        return False
    
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()