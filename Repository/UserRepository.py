from Models.user import User
from extencion import db

class UserRepository:
    @staticmethod
    def create(username, email, password):
        user = User(
            username = username,
            email = email,
            password = password
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def find_user_by_id(id):
        return User.query.get(id)