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


