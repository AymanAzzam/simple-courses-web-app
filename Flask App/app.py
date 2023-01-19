from flask import Flask, render_template
import database as db

app = Flask(__name__)


@app.route('/')
def hello():
    conn = db.connect_database()
    courses = db.select_courses(conn)

    return render_template('index.html', courses=courses)

