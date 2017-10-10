
from flask import Flask, render_template, request, session, redirect, flash
app = Flask(__name__)

app.secret_key = "123" # add secret_key for sessions

@app.route('/') # root route
def index():
	# if the following varialbes are not in session:
	# creates empty variable 
	if 'name' not in session: 
		session['name'] = "" 
	if 'location' not in session: 
		session['location'] = ""
	if 'language' not in session: 
		session['language'] = ""
	if 'description' not in session: 
		session['description'] = ""
	return render_template('index.html') # renders index.html as root

@app.route('/result', methods=['GET','POST'])
def create_user():
	# inputs will be set to its corresponding session variable
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['description'] = request.form['description']

	if len(session['name'])<1: # if name is empty
		flash("Please enter your name") # error
	elif session['location'] == 'Location': # if Location is still set to the default
		flash("Please select your Dojo Location")
	elif session['language'] == 'Language': # if language is still set to the default
		flash("Please select your favorite language")
	elif len(session['description'])>120: # if comment box is over 120 characters
		flash("Comment must be less than 120 characters")
	else: # else (no error), renders the results.html template
		return render_template('results.html', name=session['name'], location=session['location'], language=session['language'], description=session['description'])
	return redirect('/') # if error, redirects back to the root

app.run(debug=True)