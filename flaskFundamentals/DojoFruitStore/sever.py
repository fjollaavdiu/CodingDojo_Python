import os
os.environ["FLASK_ENV"] = "development"
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import datetime

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=["POST"])
def checkout():
    print("--POST INFO OBTAINED--")
    print("Name:", request.form['name'])
    print("Student ID:", request.form['studentid'])
    print("Dojo:", request.form['dojo'])
    print("Apples:", request.form['apples'])
    print("Oranges:", request.form['oranges'])
    print("Cherries:", request.form['cherries'])
    print("Peaches:", request.form['peaches'])

    name = request.form['name']
    studentid = request.form['studentid']
    apples = request.form['apples']
    oranges = request.form['oranges']
    cherries = request.form['cherries']
    peaches = request.form['peaches']
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    return render_template("checkout.html", name = name, studentid = studentid, apples = int(apples), oranges = int(oranges), cherries = int(cherries), peaches = int(peaches), timestamp = timestamp)

if __name__=="__main__":
    app.run(debug=True)