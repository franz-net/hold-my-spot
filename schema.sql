drop table users cascade;
drop table events cascade;
drop table event_admins;
drop table event_attendees;

CREATE TABLE IF NOT EXISTS users (
	id serial PRIMARY KEY,
	name varchar(50),
	last_name varchar(50),
	phone varchar(15),
	email text NOT NULL unique,
	password text
);

CREATE TABLE IF NOT EXISTS events(
    id serial PRIMARY KEY,
    title text NOT NULL,
    description TEXT,
    event_date date NOT NULL,
    event_time time NOT NULL,
    address text,
    capacity int NOT NULL,
    phone varchar(15) NOT NULL,
    email text NOT NULL
);

CREATE TABLE IF NOT EXISTS event_admins(
    user_id int REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
    event_id int REFERENCES events(id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT event_admins_pkey PRIMARY KEY(user_id, event_id)
);


CREATE TABLE IF NOT EXISTS reservations(
    reservation_id serial UNIQUE,
    user_id int REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
    event_id int REFERENCES events(id) ON UPDATE CASCADE ON DELETE CASCADE,
    attendance int DEFAULT 0,
    CONSTRAINT reservations_pkey PRIMARY KEY(reservation_id, user_id, event_id)
);