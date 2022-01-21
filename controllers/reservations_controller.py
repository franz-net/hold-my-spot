from crypt import methods
from flask import Blueprint, redirect, session, request, render_template
from models.events import get_event_by_id
from models.reservations import add_reservation, cancel_reservation, get_reservation_details, mark_attendance
from models.user import add_user, get_user_by_email

reservations_controller = Blueprint("reservations_controller", __name__)

@reservations_controller.route('/reservations/delete', methods=["POST"])
def delete_reservation():
    if not session.get('user_id'):
        return redirect('/login')
    else:
        reservation_id = request.form.get('reservation_id')
        event_id = request.form.get('event_id')
        cancel_reservation(reservation_id)
        if event_id is None:
            return redirect('/dashboard')
        else:
            return redirect('/events/'+str(event_id))


@reservations_controller.route('/reservations/attendee/add', methods=["POST"])
def admin_add_attendee():
    if session.get('user_id') or request.form.get('source') == 'external':
        email = request.form.get('email')

        user_id = get_user_by_email(email)
        if user_id is None:
            name = request.form.get('name')
            user_id = add_user(email, name, None, None, None)
        else:
            user_id = user_id['id']
            
        event_id = request.form.get('event_id')
        reservation_id = add_reservation(event_id, user_id)
        if request.form.get('source') == 'external':
            return redirect('/reservations/'+str(reservation_id)+'?external=1')
        else:
            return redirect('/events/'+str(event_id))
    else:
        return redirect('/login')

@reservations_controller.route('/reservations/<confirmation>')
def view_reservation(confirmation):
    if session.get('user_id') or request.args.get('external') == '1':
        
        reservation_details = get_reservation_details(confirmation)
        url = request.url_root + 'events/checkin' + '?confirmation=' + str(confirmation)
        if request.args.get('external') == '1':
            external = True
        else:
            external = False
        return render_template('reservation.html', reservation=reservation_details, url = url, external = external)
    else:
        return redirect('/login')

@reservations_controller.route('/event/register', methods=["GET"])
def create_reservation_from_url():

    event_id = request.args.get('event')
    event_data = get_event_by_id(event_id)

    if not session.get('user_id'):
        email = None
    else:
        email = session.get('email')

    return render_template('event_registration.html', user=email, event = event_data)

@reservations_controller.route('/events/checkin', methods=["GET"])
def reservation_checkin():
    reservation_id = int(request.args.get('confirmation'))
    print("---------" + str(reservation_id))
    mark_attendance(reservation_id, 1)
    if not session.get('user_id'):
        return redirect('/reservations/'+str(reservation_id))
    else:
        return redirect('/reservations/'+str(reservation_id)+'?external=1')

    