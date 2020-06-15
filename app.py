from flask import Flask, render_template
from forms import RegistartionForm

app = Flask(__name__)
app.secret_key = 'replace later'

@app.route('/', methods=['GET', 'POST'])
def index():
	form = RegistartionForm()
	if form.validate_on_submit():
		return "Success !!"

	return render_template("index.html", form=form)

if __name__ == "__main__":
	app.run(debug=True)