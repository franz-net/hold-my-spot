CREATE TABLE IF NOT EXISTS users (
	id serial PRIMARY KEY,
	name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	phone varchar(15) NOT NULL,
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
    url text,
    phone varchar(15) NOT NULL,
    email text NOT NULL
);

CREATE TABLE IF NOT EXISTS event_admins(
    user_id int REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
    event_id int REFERENCES events(id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT event_admins_pkey PRIMARY KEY(user_id, event_id)
);


CREATE TABLE IF NOT EXISTS event_attendees(
    user_id int REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
    event_id int REFERENCES events(id) ON UPDATE CASCADE ON DELETE CASCADE,
    attendance int DEFAULT 0,
    CONSTRAINT event_attendees_pkey PRIMARY KEY(user_id, event_id)
);