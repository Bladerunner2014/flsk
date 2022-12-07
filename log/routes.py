from flask import render_template
from log import app
from log.forms import SignUpForm, LoginForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def signup():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
		db.session.add(user)
		db.session.commit()
		flash('you registered successfully', 'success')
		return redirect(url_for('home'))
	return render_template('SignUp.html', form=form)