from database import sql_select, sql_write

#Create event
def add_event(title, description, event_date, event_time, address, capacity):
    query = "insert into events (title, description, event_date, event_time, address, capacity) values (%s,%s,%s,%s,%s)"
    params = [title, description, event_date, event_time, capacity]
    sql_write(query, params)
    return

#Return single event
def get_event_by_id(eventid):
    query = "select * from events where id = %s"
    event = sql_select(query, [eventid])
    if len(event) > 0:
        return event[0]
    else:
        return None

#Add event admin user
def add_event_admin(eventid, userid):
    query = "insert into event_admins (user_id, event_id) values (%s, %s)"
    params = [userid, eventid]
    sql_write(query, params)
    return

#Remove event admin user
def remove_event_admin(eventid, userid):
    query = "delete from event_admins where user_id = %s and event_id = %s"
    params = [userid, eventid]
    sql_write(query, params)
    return

#Update single event
def update_event(eventid, title, description, event_date, event_time, address, capacity):
    query = "update events set title = %s, description = %s, event_date = %s, event_time = %s, address = %s, capacity = %s where id = %s"
    params = [title, description, event_date, event_time, address, capacity, eventid]
    sql_write(query, params)
    return

#Register Attendee
def add_attendee(eventid, userid):
    query = "insert into event_attendees (user_id, event_id) values (%s, %s)"
    params = [userid, eventid]
    sql_write(query, params)
    return

#Unregister Attendee
def remove_attendee(eventid, userid):
    query = "delete from event_attendees where user_id = %s and event_id = %s"
    params = [userid, eventid]
    sql_write(query, params)
    return

#Checkin the attendee
def mark_attendance(eventid, userid, attendance):
    query = "update event_attendees set attendance = %s where user_id = %s and event_id = %s"
    params = [attendance, userid, eventid]
    sql_write(query, params)
    return

#See how many seats are left
def check_event_capacity(eventid):
    query = "select capacity from events where id = %s"
    capacity = sql_select(query, [eventid])[0]

    query = "select count(*) from event_attendees where event_id = %s and attendance = 1"
    total_attendance = sql_select(query, [eventid])[0]

    return capacity - total_attendance

# Return list of events by attendee
def get_event_by_name(event_name):
    query = "select * from events where title = %s"
    event = sql_select(query, [event_name])
    if len(event) > 0:
        return event
    else:
        return None

# Return list of events by admin
