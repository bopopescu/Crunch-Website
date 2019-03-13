from flask import Flask, current_app
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
login = LoginManager(app)

from app.api import api as api_bp
app.register_blueprint(api_bp)

from app.login import login_bp as login_bp
app.register_blueprint(login_bp)

from app.signup import signup_bp as signup_bp
app.register_blueprint(signup_bp)

from app.search import search_bp as search_bp
app.register_blueprint(search_bp)