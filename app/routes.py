from app import app
from app.forms import LoginForm
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'rhys' }
    return render_template('index.html', user=user)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)