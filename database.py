import os
import psycopg2
from psycopg2.extras import DictCursor

DB_URL = os.environ.get("DATABASE_URL", "dbname=hold-my-spot")

def sql_select(query, args=None):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor(cursor_factory=DictCursor)
    cur.execute(query, args)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res

def sql_write(query, args=None):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    cur.close()
    conn.close()
    return
