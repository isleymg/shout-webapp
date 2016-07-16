from shout import app
from shout import forms
from flask import render_template
from flask import request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/blog')
def blog():
	return render_template('blog.html')	

@app.route('/blog/add')
def blog_add_post():
	return render_template('blog_add_post.html')    