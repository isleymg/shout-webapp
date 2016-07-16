from shout import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



@app.route('/map/')
def map(name=None):
	return render_template('map.html', name=name)
