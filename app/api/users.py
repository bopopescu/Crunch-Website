from app.api import api
from app import Database
import mysql.connector
import json


@api.route('/create_user', methods=['POST'])
def create_user(user_info):
    data = json.loads(user_info)
    email = data["email"]
    userName = data["userName"]
    passwordHash = data["passwordHash"]
    fullName = data["fullName"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "INSERT INTO users (email, userName, passwordHash, fullName) VALUES (%s, %s, %s, %s)"
    values = (email, userName, passwordHash, fullName)
    result = Database.execStatement(myDb, sqlString, values)
    myDb.commit()
    #return(result)



@api.route('/check_user',methods=['GET'])
def check_user(user_info):
    data = json.loads(user_info)
    email = data["email"]
    userName = data["userName"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString_Email = "SELECT email FROM users WHERE email = " + "'" + email + "'"
    sqlString_UserName = "SELECT userName FROM users WHERE userName = " + "'" + userName + "'"
    result1 = Database.selectStatement(myDb, sqlString_Email)
    result2 = Database.selectStatement(myDb, sqlString_UserName)
    if (result1.rowcount != 0):
        return 'email taken'
    elif (result2.rowcount != 0):
        return 'username taken'
    else:
        return 'clear'




@api.route('/get_user', methods=['GET'])
def get_user(login_info):
    data = json.loads(login_info)
    email = data["email"]
    passwordHash = data["passwordhash"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "SELECT passwordHash, userName FROM users WHERE email = " + "'" + email + "'"
    result = Database.selectStatement(myDb, sqlString)
    if(result.rowcount == 1):
        fetch = result.fetchone()
        if (fetch[0] == passwordHash):
            return fetch[1]
    else:
        return False

