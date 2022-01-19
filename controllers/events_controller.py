from flask import Blueprint, redirect, session, request, render_template
from models.events import add_event, add_event_admin, get_capacity_left, get_events_by_admin, get_events_by_attendee, delete_event, get_event_by_id, update_event, get_attendees_by_event
from datetime import datetime

events_controller = Blueprint("events_controller", __name__)


@events_controller.route('/dashboard')
def show_dashboard():
    if not session.get('user_id'):
        return redirect('/login')
    else:
        attendee_events = get_events_by_attendee(session.get('user_id'))
        admin_events = get_events_by_admin(session.get('user_id'))
        base_url = request.url_root + 'reserve/'
        return render_template('dashboard.html', admin_events = admin_events, attendee_events = attendee_events, base_url = base_url)

@events_controller.route('/events/create')
def show_create_events():
    if not session.get('user_id'):
        return redirect('/login')
    else:
        return render_template('create_event.html')

@events_controller.route('/events/add', methods=["POST"])
def create_event():
    if not session.get('user_id'):
        return redirect('/login')
    else:
        title = request.form.get('title')
        description = request.form.get('description')
        event_date = request.form.get('event_date')
        event_time = request.form.get('event_time')
        capacity = request.form.get('capacity')
        address = request.form.get('address')
        phone = request.form.get('phone')
        email = request.form.get('email')

        event_id = add_event(title, description, event_date, event_time, address, capacity, phone, email)

        add_event_admin(event_id, session.get('user_id'))

        return redirect('/dashboard')

@events_controller.route('/events/<eventid>')
def view_event(eventid):
    if not session.get('user_id'):
        return redirect('/login')
    else:
        event = get_event_by_id(eventid)

        print(event['event_date'])

        date_form = datetime.strptime(event['event_date'], '%m/%d/%Y')
        date_form = date_form.strftime('%Y-%m-%d')
        reservations = get_capacity_left(eventid)
        event['capacity'] = f'{event["capacity"]}/{event["capacity"] - reservations}'
        attendee_list = get_attendees_by_event(eventid)
        base_url = request.url_root + 'reserve/'
        return render_template('event.html', event_data = event, attendee_data = attendee_list, date_form = date_form, base_url= base_url)

@events_controller.route('/events/update', methods=["POST"])
def update_event_data():
    if not session.get('user_id'):
        return redirect('/login')
    else:
        eventid = request.form.get('id')
        print(eventid)
        title = request.form.get('title')
        description = request.form.get('description')
        event_date = request.form.get('event_date')
        event_time = request.form.get('event_time')
        capacity = request.form.get('capacity')
        address = request.form.get('address')
        phone = request.form.get('phone')
        email = request.form.get('email')
    update_event(eventid, title, description, event_date, event_time, address, capacity, phone, email)
    return redirect('/events/' + str(eventid))


@events_controller.route('/events/delete', methods=["POST"])
def remove_event():
    if not session.get('user_id'):
        return redirect('/login')
    else:
        eventid = request.form.get('event_id')
        delete_event(eventid)
        return redirect('/dashboard')

@events_controller.route('/reservations/<eventid>') ## MISSING CORRESPONDING VIEW!!
def view_reservation(eventid):
    if not session.get('user_id'):
        return redirect('/login')
    else:
        event = get_event_by_id(eventid)
        reservation_id = str(session.get('user_id')) + '+' + str(eventid)
        return render_template('reservation.html', event_data = event, reservation = reservation_id)