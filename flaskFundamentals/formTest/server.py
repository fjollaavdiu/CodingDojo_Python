import os
os.environ["FLASK_ENV"] = "development"
from flask import Flask, render_template, request, redirect,
app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=["POST"])
def users():
    print("name:",request.form['name'])
    print("email:",request.form['email'])

    name = request.form['name']
    email= request.form['email']
    return render_template("users.html",name=name, email=email)
if __name__=="__main__":
    app.run(debug=True)
