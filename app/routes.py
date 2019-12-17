from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Javier'}
    posts = [
        {
            'author': {'username': 'Javier'},
            'body': 'Beautiful Day in the Central Valley'
        },
        {
            'author': {'username': 'Mochi'},
            'body': 'Where my money at?!'
        }

    ]
    return render_template('index.html', title="Home", user=user, posts=posts)
