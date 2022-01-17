from flask import Blueprint, redirect, session, request, render_template, jsonify
from models.user import add_user, get_user_by_email
import bcrypt

user_controller = Blueprint("user_controller", __name__)

@user_controller.route('/signup', methods=["POST"])
def register_user():
    name = request.form.get('first-name')
    lname = request.form.get('last-name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    password = bcrypt.hashpw(request.form.get('password').encode(), bcrypt.gensalt())

    add_user(email, name, lname, phone, password.decode())
    return redirect('/')

@user_controller.route('/validate_email', methods=["POST"])
def check_email_in_use():
    email = request.form.get('email')

    if get_user_by_email(email) is not None:
        response = jsonify('<span style=\'color:red;\'>Email already in use</span>')
        response.status_code = 200
        return response
    else:
        response = jsonify('<span style=\'color:green;\'>Email available</span>')
        response.status_code = 200
        return response