from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = "my_secret_string"

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('test.html')

from app.api import api as api_bp
app.register_blueprint(api_bp)

from app.login import login_bp as login_bp
app.register_blueprint(login_bp)

from app.search import search_bp as search_bp
app.register_blueprint(search_bp)

from app.signup import signup_bp as signup_bp
app.register_blueprint(signup_bp)

from app.newsletter import newsletter_bp as newsletter_bp
app.register_blueprint(newsletter_bp)

from app.support import support_bp as support_bp
app.register_blueprint(support_bp)