from flask import Flask, redirect, url_for, request, render_template, make_response, session, escape, flash
import sys
import pprint
app = Flask(__name__)
app.secret_key = 'any random string'
@app.route('/')
def index():
   if 'username' in session and 'hmit' in session:
      username = session['username']
      return 'Logged in as' + username +'<br>' + "<b><a href='/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href='/login'></b>"+ "click here to log in </b></a>"
@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      session['hmit'] = 2
      return redirect(url_for('index'))
   return '''
      <form action="" method = "post">
         <p><input type = "text" name="username"></p>
         <p><input type = submit value = Login></p>
      </form>
   '''
@app.route('/logout')
def logout():
   session.pop('username', None)
   session.pop('hmit', None)
   return redirect(url_for('index'))

# @app.route('/flash-message')
# def index():
#    return render_template('index.html')
if __name__ == '__main__':
   app.run(debug=True)