from flask import Flask, request, flash, url_for, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] ='random string'

db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    addr = db.Column(db.String(400))
    pin = db.Column(db.String(100))

def __init__(self, name, city, addr, pin):
    self.name = name
    self.city = city
    self.addr = addr
    self.pin = pin

@app.route('/')
def show_all():
    return render_template('show_all.html', students = students.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['pin']:
            flash('Please enter all the fields', 'error')
        else:
            form = request.form
            student = students(name = form['name'], city = form['city'], addr = form['addr'], pin = form['pin'])
            db.session.add(student)
            db.session.commit()
            flash('Record was added successfully')
            return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)