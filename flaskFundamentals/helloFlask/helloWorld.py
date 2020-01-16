from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World 123!'
if __name__ == '__main__':
    app.run(debug=True)