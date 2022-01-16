create table users (
	id serial primary key,
	name VARCHAR(50) not null,
	last_name VARCHAR(50) not null,
	phone VARCHAR(15) not null,
	email text not null unique,
	password text not null
);

create table events(
    id serial primary key,
    title TEXT not null,
    description TEXT,
    event_date date not null,
    event_time time not null
)

create table event_admins(
    user_id int not null,
    event_id int not null,
    primary key(user_id, event_id),
    constraint fk_user FOREIGN KEY(user_id) REFERENCES users(id),
    constraint fk_event FOREIGN KEY(event_id) REFERENCES events(id) on delete cascade
)
