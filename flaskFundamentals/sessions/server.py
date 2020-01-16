import os
os.environ["FLASK_ENV"] = "development"
from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
# Sessions also require a secret key to run so you'll have to set a secret key in your server.py as follows:
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=["POST"])
def users():
    print("name:",request.form['name'])
    print("email:",request.form['email'])

# #   session['name'] = request.form['name']
# #   session['email']= request.form['email']
#     return render_template("show.html", name=session['name'], email=session['email']))
# if __name__=="__main__":
#     app.run(debug=True)
