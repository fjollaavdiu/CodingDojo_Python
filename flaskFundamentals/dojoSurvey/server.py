import os
os.environ["FLASK_ENV"] = "development"
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/result', methods=['POST'])
def result():
    print("--POST INFOMATION CHACHED--")
    print("Name:", request.form['name'])
    print("Dojo Location:", request.form['location'])
    print("Favorite Language:", request.form['language'])
    print("Comments:", request.form['comment'])
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    return render_template("result.html", name = name, location = location, language = language, comment = comment)

if __name__=="__main__":
    app.run(debug=True)