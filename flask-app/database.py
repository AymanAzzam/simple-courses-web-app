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


def execute_query(query: str):
    usefulInfo = {'query': query}
    print(usefulInfo)

    connection = connect_database()
    with connection.cursor(DictCursor) as cur:
        try:
            cur.execute(query)
            rows = cur.fetchall()
        except Exception as e:
            print(e)
            sys.exit()

    usefulInfo = {'result': rows}
    print(usefulInfo)
    connection.close()
    return rows


def commit_query(query: str):
    usefulInfo = {'query': query}
    print(usefulInfo)

    connection = connect_database()
    with connection.cursor(DictCursor) as cur:
        try:
            cur.execute(query)
            connection.commit()
        except Exception as e:
            print(e)
            sys.exit()

    usefulInfo = {'updated records': cur.rowcount, 'record id': cur.lastrowid}
    print(usefulInfo)
    connection.close()
    return cur.lastrowid, cur.rowcount


def select_courses():
    query = f"select * from courses"
    result = execute_query(query)
    return result


def select_course(course_id):
    query = f"select * from courses where id = {course_id}"
    result = execute_query(query)
    return result[0]


def update_course(course):
    query = f'UPDATE courses SET name = "{course["name"]}", start_date = "{course["date"]}", duration = {course["duration"]}, price = {course["price"]} WHERE id = {course["id"]}'
    commit_query(query)


def insert_course(course):
    query = f'INSERT INTO courses (name, start_date, duration, price) VALUES ("{course["name"]}", "{course["date"]}", {course["duration"]}, {course["price"]})'
    commit_query(query)


def delete_course(course_id):
    query = f'DELETE FROM courses WHERE id={course_id}'
    commit_query(query)