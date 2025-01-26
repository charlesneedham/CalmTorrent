from flask import Flask, render_template
from routes.login import bp as login_bp
app = Flask(__name__)


app.register_blueprint(login_bp)
