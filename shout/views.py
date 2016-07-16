from shout import app
from flask import render_template

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('map.html', name=name)


