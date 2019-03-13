from app.search import search_bp
import json
from flask import render_template, redirect, url_for
from flask import request
from app.api import movie_search

@search_bp.route('/search_page', methods=["GET", "POST"])
def search_page():
    error = None
    if request.method == "POST":
        search_criteria = request.form.get('search_criteria', False)

        info = {
            "search": search_criteria
        }

        data = movie_search.search_movie(json.dumps(info))

        if(data == {}):
            error = "No movies of that title exist!"
            state = {
                "status": error
            }
            return json.dumps(state)
        else:
            #return data
            #return redirect("search_results.html", data=data)

            loaded_data = json.loads(data)
            return redirect(url_for("search.search_results_page", data=loaded_data))
    return render_template("search.html", error=error)

@search_bp.route('/search_results_page', methods=["GET", "POST"])
def search_results_page():
    data = request.args.get('data')
    return render_template("search_results.html", data=data)