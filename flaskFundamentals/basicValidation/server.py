import os
os.environ["FLASK_ENV"] = "development"
from flask import Flask,render_template, redirect,request,session,flash
app=Flask(__name__)
app.secret_key="KeepItSecretKeeItSafe"
@app.route('/')
def index():
    return render_template('index.html')

app.route('/process',methods =['POST'])
def process ():
    # lets do some validation here
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    else:
        flash(f"Success! Your name is {request.form['name']}.")
    return redirect('/') 
if __name__=="__main__":
    app.run(debug = True)