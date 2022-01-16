from database import sql_select, sql_write

def add_user(email, name, lastname, phone, password):
    query = "insert into users (name, lastname, phone, email, password) VALUES (%s, %s, %s, %s, %s)"
    params = [name, lastname, phone, email, password]
    sql_write(query, params)
    return

def get_user_by_email(email):
    query = "select * from users where email = %s"
    user = sql_select(query, [email])
    if len(user) > 0:
        return user[0]
    else:
        return None