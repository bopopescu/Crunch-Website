import json
from flask import render_template, redirect, request, flash
from app.login import login_bp
from app.api import users, hashing
# from flask_login import current_user, login_user

@login_bp.route('/login_page',methods=['GET','POST'])
def login_page():
    error = None

    if request.method == "POST":
        email = request.form.get('email', False)

        password = request.form.get('password', False)
        to_hash = {
            "password": password
        }
        hash = hashing.hash_password(json.dumps(to_hash))
        info = json.loads(hash)
        pH = info["passwordhash"]

        info = {
            "email": email,
            "passwordhash": pH
        }

        json_info = json.dumps(info)
        user = users.get_user(json_info)

        if(user == False):
            error = "Login information is incorrect"
            info = {
                "status": "Failure"
            }
        else:
            error = "Success"
            info = {
                "status": "Success",
                "userName": user
            }
        #return json.dumps(info)

    return render_template("login.html", error=error)


