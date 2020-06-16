from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

from forms import *
from models import *

app = Flask(__name__)
app.secret_key = 'replace later'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jrmjgfixqxbbuz:0f35893ac039693a354caf175d93db2535f69b6855c581caaf43e7f151c473bd@ec2-18-210-214-86.compute-1.amazonaws.com:5432/d6mqfeual3o5n7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/', methods=['GET', 'POST'])
def index():
	form = RegistartionForm()
	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data

		# Hashing the password
		hashed_password = pbkdf2_sha256.hash(password)

		# add user to database 
		user = User(username=username, password=hashed_password)
		db.session.add(user)
		db.session.commit()

		return redirect(url_for('login'))

	return render_template("index.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		login_user(user)
		return redirect(url_for('chat'))

	return render_template('login.html', form=form)

@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
	return "Chat Room :)"

@app.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return "User is logged out !!"


if __name__ == "__main__":
	app.run(debug=True)