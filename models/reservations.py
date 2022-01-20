from database import sql_select, sql_write
DATE_FORMAT = "%m/%d/%Y"
TIME_FORMAT = "%H:%M:%S"

#Register Attendee
def add_reservation(eventid, userid):
    query = "insert into reservations (user_id, event_id) values (%s, %s) RETURNING reservation_id"
    params = [userid, eventid]
    reservation_id = sql_write(query, params)['reservation_id']
    return reservation_id

#Unregister Attendee
def cancel_reservation(reservationid):
    query = "delete from reservations where reservation_id = %s"
    sql_write(query, [reservationid])
    return

#Checkin the attendee
def mark_attendance(reservationid, attendance):
    query = "update reservations set attendance = %s where reservation_id = %s"
    params = [attendance, reservationid]
    sql_write(query, params)
    return

#Reservation details
def get_reservation_details(reservationid):
    query = "select u.name, u.email, e.title, e.description, e.event_date, e.event_time, e.address, e.email, e.phone, ea.attendance, ea.reservation_id, ea.event_id from reservations ea join events e on ea.event_id = e.id join users u on ea.user_id = u.id where ea.reservation_id = %s"
    reservation = sql_select(query,[reservationid])
    if len(reservation) > 0:
        reservation[0]['event_date'] = reservation[0]['event_date'].strftime(DATE_FORMAT)
        reservation[0]['event_time'] = reservation[0]['event_time'].strftime(TIME_FORMAT)
        return reservation[0]
    else:
        return None