from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mark'}
    posts = [
        {
            'author': {'username': 'Sarah'},
            'body': 'Beautiful day in Atlanta!'
        },
        {
            'author': {'username': 'Carla'},
            'body': 'I love Roswell.'
        }
    ]
    return render_template('index.html', title = 'Home', user=user, posts=posts)