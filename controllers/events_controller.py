from flask import Blueprint, redirect, session, request, render_template
from models.events import add_event

events_controller = Blueprint("events_controller", __name__)


@events_controller.route('/dashboard')
def show_dashboard():
    if not session.get('user_id'):
        return render_template('login.html')
    else:
        # Grab events orderd by date, if none, show "no events today, would you like to create an event?" - link to /events/create
        # Grab events you are in charge of and display them in order of date
        return render_template('dashboard.html')