from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename
import json
app = Flask(__name__)
app.secret_key = 'random string'
app.config['UPLOAD_FOLDER'] = 'static'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
     error = None
     if request.method == 'POST':
         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
             error = 'Invalid username or password!'
         else:
             flash('You were successfully logged in')
             return redirect(url_for('index'))
     return render_template('login.html', error = error)

@app.route('/upload')
def up():
    return render_template('upload.html')
    # return (app.config['UPLOAD_FOLDER'])

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'done'

if __name__ == "__main__":
    app.run(debug=True)