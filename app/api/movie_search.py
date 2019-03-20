from app.api import api
from app import Database
import json

@api.route('/search_movie', methods=["GET"])
def search_movie(search_criteria):
    data = json.loads(search_criteria)
    search = data["search"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "SELECT * FROM titles WHERE primaryTitle LIKE " + "'" + search + "%'" + "AND titleType = 'movie'"
    result = Database.selectStatement(myDb, sqlString)
    fetch = result.fetchall()
    info = {}
    for row in fetch:
        info[row[0]] = {
            "movieID": row[0],
            "title": row[3],
            "isAdult": row[4],
            "startYear": row[5],
            "runtime": row[7],
            "genres": row[8]
        }

    return json.dumps(info)


@api.route('/get_movieID', methods=["GET"])
def get_movieID(movie_title):
    data = json.loads(movie_title)
    search = data["movieTitle"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "SELECT tconst FROM titles WHERE primaryTitle = " "'" + search + "'" + "AND titleType = 'movie'"
    result = Database.selectStatement(myDb, sqlString)
    fetch = result.fetchone()[0]
    info = {
        "titleID": fetch
    }

    return json.dumps(info)

@api.route('/get_cast', methods=["GET"])
def get_cast(movie_id):
    data = json.loads(movie_id)
    search = data["movieID"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "SELECT nconst, category, job, characters FROM moviedb.cast WHERE tconst = " "'" + search + "'"
    result = Database.selectStatement(myDb, sqlString)
    cast_fetch = result.fetchall()
    completeInfo = {}
    for row in cast_fetch:
        info = {
            "nameID": row[0]
        }
        name_request = get_names(json.dumps(info))
        name_data = json.loads(name_request)
        name = name_data["name"]
        completeInfo[row[0]] = {
            "name": name,
            "category": row[1],
            "job": row[2],
            "characters": row[3]
        }
    return json.dumps(completeInfo)



@api.route('/get_names', methods=["GET"])
def get_names(name_id):
    data = json.loads(name_id)
    search = data["nameID"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "SELECT primaryName FROM name_basic WHERE nconst = " "'" + search + "'"
    result = Database.selectStatement(myDb, sqlString)
    fetch = result.fetchone()
    info = {
        "name": fetch
    }

    return json.dumps(info)


