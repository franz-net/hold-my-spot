from flask import Flask, render_template, session
from controllers.user_controller import user_controller
from controllers.session_controller import session_controller
from controllers.events_controller import events_controller
from controllers.reservations_controller import reservations_controller
import os


SEC_KEY = os.environ.get("SECRET_KEY", "MY_SECRET")

app = Flask(__name__)
app.config['SECRET_KEY'] = SEC_KEY
app.config['SESSION_COOKIE_SECURE'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 3600
app.config['SESSION_PERMANENT'] = True
app.register_blueprint(user_controller)
app.register_blueprint(session_controller)
app.register_blueprint(events_controller)
app.register_blueprint(reservations_controller)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)