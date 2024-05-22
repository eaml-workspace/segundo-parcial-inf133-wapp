from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from database import db

class User(UserMixin, db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(120), nullable = False)
    role = db.Column(db.String(100), nullable = False, default="user")
    
    def __init__(self, username, password, role):
        self.username = username
        self.set_password(password)
        self.role(role)
    
    def set_password(password):
        return generate_password_hash(password)
    
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()
    