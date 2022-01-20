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
    if not session.get('user_id'):
        return redirect('/login')
    else:
        
        email = request.form.get('email')

        user_id = get_user_by_email(email)['id']
        if user_id is None:
            name = request.form.get('name')
            user_id = add_user(email, name, None, None, None)
            

        event_id = request.form.get('event_id')
        
        add_reservation(event_id, user_id)
                
        return redirect('/events/'+str(event_id))

@reservations_controller.route('/reservations/<confirmation>') ## MISSING CORRESPONDING VIEW!!
def view_reservation(confirmation):
    if not session.get('user_id'):
        return redirect('/login')
    else:
        reservation_details = get_reservation_details(confirmation)
        url = request.url_root + 'reservations/' + str(reservation_details['event_id']) + '?confirmation=' + str(confirmation)
        print(reservation_details)
        return render_template('reservation.html', reservation=reservation_details, url = url)