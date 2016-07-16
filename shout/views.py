from shout import app
from flask import render_template
from flask import request
from shout.api_helpers import map_point, blog_post, get_bucket, get_doc, update_doc


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resources/')
def resources():
    return render_template('resources.html')

@app.route('/faq/')
def faq():
    return render_template('faq.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/map/')
def map(name=None):
    return render_template('map.html', name=name)

@app.route('/blog/')
def blog():
    return render_template('blog.html') 

@app.route('/blog/add/')
def blog_add_post():
    return render_template('blog_add_post.html')  


# endpoints
@app.route('/plotpt', methods=['POST'])
def plot_point():
    doc = get_doc(get_bucket(), 'metadata')
    if doc is None:
        update_doc(get_bucket(), 'metadata', {'post_counter':0, 'marker_counter':0})
        doc = get_doc(get_bucket(), 'metadata')
    update_doc(get_bucket(), 'MAP' + str(doc['marker_counter']), request.get_json())
    


@app.route('/sendpost', methods=['POST'])
def receive_post():
    doc = get_doc(get_bucket(), 'metadata')
    if doc is None:
        update_doc(get_bucket(), 'metadata', {'post_counter':0, 'marker_counter':0})
        doc = get_doc(get_bucket(), 'metadata')
    update_doc(get_bucket(), 'BLOG' + str(doc['post_counter']), request.get_json())
    
  
    return render_template('blog_add_post.html')

