from flask import Flask, render_template
import os
import psycopg2

DB_URL = os.environ.get("DATABASE_URL", "dbname=hold-my-spot")
SEC_KEY = os.environ.get("SECRET_KEY", "MY_SECRET")

app = Flask(__name__)

app.config['SECRET_KEY'] = SEC_KEY

@app.route('/')
def index():
    #conn = psycopg2.connect(DB_URL)
    #cur = conn.cursor()
    #cur.execute('SELECT 1', []) # Query to check that the DB connected
    #conn.close()
    #return 'Hello, world!'
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)