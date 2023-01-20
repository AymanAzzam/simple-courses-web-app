from flask import Flask, render_template, redirect, request, jsonify
import database as db

app = Flask(__name__)
conn = db.connect_database()


@app.route('/')
def hello():
    courses = db.select_courses(conn)
    return render_template('index.html', courses=courses)

@app.route('/new')
def post():
    return render_template('post.html')

@app.route('/add', methods = ['POST'])
def add():
    course = request.form.to_dict()
    db.insert_course(conn, course)
    return redirect('/')

@app.route('/<int:course_id>/edit')
def put(course_id):
    course = db.select_course(conn, course_id)
    return render_template('put.html', course=course)

@app.route('/<int:course_id>/update', methods = ['POST'])
def update(course_id):
    course = request.form.to_dict()
    course['id'] = course_id
    db.update_course(conn, course)
    return redirect('/')

@app.route('/<int:course_id>/delete')
def delete(course_id):
    db.delete_course(conn, course_id)
    return redirect('/')