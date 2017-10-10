
from flask import Flask, render_template, request, session, redirect, flash
app = Flask(__name__)

app.secret_key = "123"
@app.route('/')
def index(): # root route
	if 'name' not in session: 
		session['name'] = ""
	if 'location' not in session: 
		session['location'] = ""
	if 'language' not in session: 
		session['language'] = ""
	if 'description' not in session: 
		session['description'] = ""
	return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def create_user():
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['description'] = request.form['description']

	if len(session['name'])<1: 
		flash("Please enter your name")
	elif session['location'] == 'Location': 
		flash("Please select your Dojo Location")
	elif session['language'] == 'Language':
		flash("Please select your favorite language")
	elif len(session['description'])>120: 
		flash("Comment must be less than 120 characters")
	else: 
		return render_template('results.html', name=session['name'], location=session['location'], language=session['language'], description=session['description'])
	return redirect('/')

app.run(debug=True)