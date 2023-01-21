from flask import Flask, render_template, redirect, request
import database as db
import os

app = Flask(__name__)

@app.route('/')
def hello():
    courses = db.select_courses()
    return render_template('index.html', courses=courses)

@app.route('/new')
def post():
    return render_template('post.html')

@app.route('/add', methods = ['POST'])
def add():
    course = request.form.to_dict()
    db.insert_course(course)
    return redirect('/')

@app.route('/<int:course_id>/edit')
def put(course_id):
    course = db.select_course(course_id)
    return render_template('put.html', course=course)

@app.route('/<int:course_id>/update', methods = ['POST'])
def update(course_id):
    course = request.form.to_dict()
    course['id'] = course_id
    db.update_course(course)
    return redirect('/')

@app.route('/<int:course_id>/delete')
def delete(course_id):
    db.delete_course(course_id)
    return redirect('/')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    # This part is added to be able to run the app inside a container
    app.run(debug=True, host='0.0.0.0', port=port)