from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index page...'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
# def hello_world():
#     return 'Hello, world!'
