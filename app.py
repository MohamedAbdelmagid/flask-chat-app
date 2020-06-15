from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from forms import *
from models import *

app = Flask(__name__)
app.secret_key = 'replace later'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jrmjgfixqxbbuz:0f35893ac039693a354caf175d93db2535f69b6855c581caaf43e7f151c473bd@ec2-18-210-214-86.compute-1.amazonaws.com:5432/d6mqfeual3o5n7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	form = RegistartionForm()
	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data

		# add user to database 
		user = User(username=username, password=password)
		db.session.add(user)
		db.session.commit()
		return "Success !! inserted into DB"

	return render_template("index.html", form=form)

if __name__ == "__main__":
	app.run(debug=True)