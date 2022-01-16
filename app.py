from flask import Flask, render_template
from controllers.user_controller import user_controller
from controllers.session_controller import session_controller
import os



SEC_KEY = os.environ.get("SECRET_KEY", "MY_SECRET")

app = Flask(__name__)
app.config['SECRET_KEY'] = SEC_KEY
app.register_blueprint(user_controller)
app.register_blueprint(session_controller)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)