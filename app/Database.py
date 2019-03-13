import mysql.connector
import mysqlx

def dbConnection():
    dbHost = 'localhost'
    dbUser = 'Hershil'
    dbPassword = 'H3r5h!l007'
    db = 'moviedb'

    mydb = mysql.connector.connect(host=dbHost, user=dbUser, password=dbPassword, database=db)
    if(mydb):
        return mydb
    else:
        return None

def execStatement(dbConnection, sqlQuery, values):
    dbCursor = dbConnection.cursor(buffered=True)
    dbCursor.execute(sqlQuery, values)
    return dbCursor

def selectStatement(dbConnection, sqlQuery):
    dbCursor = dbConnection.cursor(buffered=True)
    dbCursor.execute(sqlQuery)
    return dbCursor
