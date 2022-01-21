from database import sql_select, sql_write

DATE_FORMAT = "%m/%d/%Y"
TIME_FORMAT = "%H:%M:%S"

#Create event
def add_event(title, description, event_date, event_time, address, capacity, phone, email):
    query = "insert into events (title, description, event_date, event_time, address, capacity, phone, email) values (%s,%s,%s,%s, %s, %s, %s, %s) RETURNING id;"
    params = [title, description, event_date, event_time, address, capacity, phone, email]
    inserted = sql_write(query, params)['id']
    return inserted

#Return single event
def get_event_by_id(eventid):
    query = "select * from events where id = %s"
    event = sql_select(query, [eventid])
    if len(event) > 0:
        event[0]['event_date'] = event[0]['event_date'].strftime(DATE_FORMAT)
        event[0]['event_time'] = event[0]['event_time'].strftime(TIME_FORMAT)
        return event[0]
    else:
        return None

#Add event admin user
def add_event_admin(eventid, userid):
    query = "insert into event_admins (user_id, event_id) values (%s, %s)"
    params = [userid, eventid]
    sql_write(query, params)
    return


#Update single event
def update_event(eventid, title, description, event_date, event_time, address, capacity, phone, email):
    query = "update events set title = %s, description = %s, event_date = %s, event_time = %s, address = %s, capacity = %s, phone = %s, email = %s where id = %s"
    params = [title, description, event_date, event_time, address, capacity, phone, email, eventid]
    sql_write(query, params)
    return

#See how many seats are left
def get_capacity_left(eventid):
    query = "select count(*) AS reservations from reservations where event_id = %s"
    reserved = sql_select(query,[eventid])[0]
    return reserved['reservations']

#Return list of events by attendee
def get_events_by_attendee(userid):
    query = "select e.id, e.title, e.description, e.event_date, e.event_time, e.address, ea.reservation_id from reservations ea join events e on ea.event_id = e.id where ea.user_id = %s;"
    events = sql_select(query, [userid])
    for row in events:
        row['event_date'] = row['event_date'].strftime(DATE_FORMAT)
        row['event_time'] = row['event_time'].strftime(TIME_FORMAT)
    return events

#Return list of events by admin
def get_events_by_admin(userid):
    query = "select e.id, e.title, e.description, e.event_date, e.event_time, e.address, e.capacity from event_admins ea join events e on ea.event_id = e.id where ea.user_id = %s;"
    events = sql_select(query, [userid])
    for row in events:
        row['event_date'] = row['event_date'].strftime(DATE_FORMAT)
        row['event_time'] = row['event_time'].strftime(TIME_FORMAT)
    return events

#Return list of attendees by eventid
def get_attendees_by_event(eventid):
    query = "select u.id, u.name, u.last_name, u.phone, u.email, ea.reservation_id, ea.attendance from reservations ea join users u on ea.user_id = u.id where ea.event_id = %s"
    attendee_list = sql_select(query, [eventid])
    return attendee_list

def delete_event(eventid):
    query = "delete from events where id = %s;"
    sql_write(query, [eventid])
    return
