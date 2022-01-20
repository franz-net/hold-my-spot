from database import sql_write

#Register Attendee
def add_reservation(eventid, userid):
    query = "insert into event_attendees (user_id, event_id) values (%s, %s) RETURNING reservation_id"
    params = [userid, eventid]
    reservation_id = sql_write(query, params)['reservation_id']
    return reservation_id

#Unregister Attendee
def cancel_reservation(reservationid):
    query = "delete from event_attendees where reservation_id = %s"
    sql_write(query, [reservationid])
    return

#Checkin the attendee
def mark_attendance(reservationid, attendance):
    query = "update event_attendees set attendance = %s where reservation_id = %s"
    params = [attendance, reservationid]
    sql_write(query, params)
    return