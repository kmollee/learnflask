from flask import (
    Flask, render_template, redirect, url_for, request, session, flash, g)
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# create the application object
app = Flask(__name__)
bcrypt = Bcrypt(app)
# load config from file obj
app.config.from_object('config.DevelopmentConfig')
# load config from os env variable
# app.config.from_object(os.environ['APP_SETTINGS'])
# create the sqlalchemy object
db = SQLAlchemy(app)

from models import *


def login_require(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('you have to login first')
            return redirect(url_for('login'))
    return wrap

# http://flask.pocoo.org/docs/0.11/api/#flask.g


@app.route('/')
@login_require
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again'
        else:
            session['logged_in'] = True
            flash('You were login.')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_require
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)
