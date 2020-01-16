import os
os.environ["FLASK_ENV"] = "development"
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    student_info=(
        {'name':'Michael','age':35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    )
    return render_template("index1.html", random_numbers=[1,13,5,7,8,9], students=student_info)
if __name__=="__main__":
    app.run(debug=True)