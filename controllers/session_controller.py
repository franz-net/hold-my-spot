from flask import Blueprint, session, request, redirect, render_template
from models.user import get_user_by_email
import bcrypt

session_controller = Blueprint("session_controller", __name__)

@session_controller.route('/login')
def login():
    if not session.get('user_id'):
        error=request.args.get('error')
        message=request.args.get('message')
        return render_template('login.html', error=error, message=message)
    else:
        return redirect('/dashboard')


@session_controller.route('/auth', methods=["POST"])
def authenticate_user():
    username = request.form.get('email')
    password = request.form.get('password')

    user = get_user_by_email(username)
    if user and bcrypt.checkpw(password.encode(), user['password'].encode()):
        session['user_id'] = user['id']
        session['name'] = user['name']
        session['email'] = user['email']
        return redirect('/dashboard')
    else:
        return redirect('/login?error=Invalid+Credentials')

@session_controller.route('/logout')
def deauthenticate_user():
    session.clear()
    return redirect('/')