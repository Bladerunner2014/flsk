from flask import flash, render_template, redirect, url_for
from log import app, db, bcrypt
from log.forms import SignUpForm, LoginForm
from log.models import User
from flask_login import login_user, current_user, logout_user


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash('you signed up successfully', 'success')
        return redirect(url_for('home'))
    return render_template('SignUp.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('you logged in successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('email or password is wrong', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('you logged out successfully', 'success')
    return redirect(url_for('home'))
