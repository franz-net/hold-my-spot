create table users (
	id serial primary key,
	name VARCHAR(50) not null,
	last_name VARCHAR(50) not null,
	phone VARCHAR(15) not null,
	email text not null unique,
	password text not null
);

create table orgs (
    id serial primary key,
    name TEXT not null,
    
)