import os
os.environ["FLASK_ENV"] = "development"
from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name="fjolla", last="avdiu", list=[1,2,3])

if __name__=="__main__":
    app.run(debug=True)