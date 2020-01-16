import os
os.environ["FLASK_ENV"] = "development"
from flask import Flask, render_template
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # we'll talk about the following two lines after we learn a little more about forms
    Name = request.form['name']
    Email = request.form['email']
    # redirects back to the '/' route
    # return redirect('/')
    # To send you to the success.html that has the view with the information submitted
    return render_template('success.html')
@app.route('/show')
def show_user():
    return render_template('user.html', name = '', email='')
if __name__=="__main__":
    # run our server
    app.run(debug=True) 