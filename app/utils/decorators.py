from functools import wraps
from flask import jsonify, flash
from flask_login import current_user

def decorator(func):
    @wraps(func)
    def has_role(role):
        if current_user.role == role:
            return True
        else:
            return False
    return func(has_role)
