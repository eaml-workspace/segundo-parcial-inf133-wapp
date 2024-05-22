from flask import redirect, render_template, jsonify
from modells.user_model import User
import json

def login_user(user):
    return redirect(
        user=user,
        
    )