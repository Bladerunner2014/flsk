from flask import render_template
from log import app
from log.forms import SignUpForm, LoginForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register')
def signup():
    form = SignUpForm()
    return render_template('SignUp.html', form = form)
