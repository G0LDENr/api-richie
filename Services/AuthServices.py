from Repository.UserRepository import UserRepository
from flask_jwt_extended import create_access_token 
from datetime import timedelta


class authService:
    @staticmethod
    def register(username, email, password):
        user = UserRepository.create(username, email, password)
        return user
    
    @staticmethod
    def find_by_id(id):
        return UserRepository.find_user_by_id(id)
    
    @staticmethod
    def login(username, password):
        user = UserRepository.find_by_username(username)
        check = user.check_password(password)
        if not user:
            return None
        
        claims = {
            "username": user.username,
        }

        token = create_access_token(identity=user.id, additional_claims=claims, expires_delta=timedelta(hours=8))
        return {
            "access_token": token,
            "user": user
        }