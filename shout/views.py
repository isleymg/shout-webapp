from shout import app
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


@app.route('/map/')
def map(name=None):
	return render_template('map.html', name=name)

@app.route('/blog')
def blog():
	return render_template('blog.html')	

@app.route('/blog/add')
def blog_add_post():
	return render_template('blog_add_post.html')  

	
# endpoints
@app.route('/sendform', methods=['POST'])
def receive_form():
	content = request.values
	data_id = content.get('data_id')
	date = content.get('date')
	category = content.get('category')
	latitude = content.get('latitude')
	longitude = content.get('longitude')
    # todo: post to couchbase

@app.route('/plotpt', methods=['POST'])
def plot_point():
	content = request.values
	blog_id = content.get('blog_id')
	date = content.get('date')
	title = content.get('title')
	body = content.get('body')
	latitude = content.get('latitude')
	longitude = content.get('longitude')
	# todo: post to couchbase
  