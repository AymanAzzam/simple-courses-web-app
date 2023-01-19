import pymysql
from pymysql.cursors import DictCursor
import sys
import os

########################## [DATABASE CONFIGURATIONS] ##################################
dbHost = os.environ['DB_HOST']
dbUser = os.environ['DB_USERNAME']
dbPassword = os.environ['DB_PASSWORD']
dbName = os.environ['DB_NAME']

def connect_database():
    try:
        connection = pymysql.connect(host=dbHost, user=dbUser, password=dbPassword, database=dbName, connect_timeout=5)
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()

    return connection


def select_query(connection, query: str):
    with connection.cursor(DictCursor) as cur:
        try:
            cur.execute(query)
            rows = cur.fetchall()
        except Exception as e:
            print(e)
            sys.exit()

    usefulInfo = {'query': query, 'result': rows}
    print(usefulInfo)
    return rows


def select_courses(connection):
    query = "select * from courses"
    result = select_query(connection, query)
    return result