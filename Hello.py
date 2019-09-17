from flask import Flask, redirect, url_for, request, render_template
import jinja2
import pprint
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')
@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template('result.html', result = result)

#
# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' %name
#
# @app.route('/login', methods=['POST','GET'])
# def login():
#    if request.method == 'POST':
#       return 'post'
#       print(request.method)
#       user = request.form['name']
#       return redirect(url_for('success', name = user))
#    else:
#       user = request.args.get('name')
#       # return user
#       return redirect(url_for('success', name = user))
#
#
# @app.route('/hello/<user>')
# def hello_name(user):
#       return render_template('hello.html', name = user)
# @app.route('/result')
# def result():
#    dict1 = {'Phy': 50, 'Che': 30, 'Maths': 90}
#    return render_template('result.html', result = dict1)
if __name__ == '__main__':
   app.run(debug=True)