from flask import Flask, render_template, request, url_for, redirect
from language_descriptions import languages

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/about')
def about_page():
	return render_template('about.html')

@app.route('/languages')
def languages_page():
	return render_template('languages.html', languages=languages)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
	if request.method == 'POST':
		# When the form is submitted, redirect to the home page
		return redirect(url_for('home_page'))
	else:
		# Otherwise, show the login form
		return render_template('login.html')

if __name__ == "__main__":
	app.run(debug=True)