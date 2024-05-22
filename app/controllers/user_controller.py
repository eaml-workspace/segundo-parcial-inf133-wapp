from flask import redirect, request, flash, url_for, Blueprint
from flask_login import login_required, current_user
from modells.user_model import User
from werkzeug.security import check_password_hash
from views import user_view

user_bp= Blueprint("/users", __name__)

@user_bp.route("/", methods="GET")
def index():
    print()

@user_bp.route("/users", methods=["GET"])
def registro(user):
    print("")

