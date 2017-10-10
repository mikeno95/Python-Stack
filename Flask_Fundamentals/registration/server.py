from flask import Flask, render_template, redirect, session, request, flash
import re
from datetime import date, datetime

app = Flask(__name__)

app.secret_key = "shhhhhhhhh. it's a secret" # set secret key to use sessions

# email regex to validate email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def checkString(string): # function to validate if string contains digits
	# takes in string argument
	for i in string: # loop through each index in string
		if i.isdigit(): # checks if the string at that index is a digit
			return False # if there is a digit, returns false
	return True # if no digit, returns true

def checkPW(password): # function to validate if password contain at least 1 uppercase and 1 digit
	# takes in password argument 
	count_int = 0 # set count variables to 0
	count_up = 0
	for i in password: # loop through each index in password
		if i.isupper(): # if the string at that index is a upper case
			count_up+=1 # add 1 to count_up
		elif i.isdigit(): # if the string at that index is a digit 
			count_int+=1 # add 1 to count_int
	if count_int>0 and count_up>0: # check if count_int and count_up are higher than 0
		return True # returns true 
	return False # if no int or uppercase, returns false
	
def checkBirthday(strbday): # function to validate if birthday is from the past
	# takes in strbday argument
	# variable bday is set to the converted strbday to match type with datetime.date
	bday = datetime.strptime(strbday, '%Y-%m-%d').date()
	# variable today is set to the current date
	today = date.today()
	if bday>today: # if bday is greater than today (future)
		return False # returns false
	return True # otherwise, returns true

@app.route('/') # root route
def index():
	# checks if variables are in session, and if not, set those variables as empty string
	if 'email' not in session: 
		session['email'] = ''
	if 'first_name' not in session:
		session['first_name'] = ''
	if 'last_name' not in session: 
		session['last_name'] = ''
	if 'password' not in session: 
		session['password'] = ''
	return render_template('index.html') # renders index.html

@app.route('/results', methods=['POST']) # /results route is POST
def result():
	# set sessions variables to corresponding form inputs
	session['email'] = request.form['email']
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['bday'] = request.form['bday']
	session['password'] = request.form['psw']
	cpw = request.form['cpsw'] # confirm password doesn't need to be a session because it's just for checking password

	# conditionals for validation and flash messages
	# if email, first_name, or last_name are empty
	if len(session['email']) < 1 or len(session['first_name'])<1 or len(session['last_name'])<1:
		flash('All fields are required and must not be blank.', 'error') 
	# else if email is not in proper form
	elif not EMAIL_REGEX.match(session['email']):
		flash('Please enter a valid email', 'error')
	# if first and last name contains numbers
	elif not checkString(session['first_name']) or not checkString(session['last_name']): 
		flash('Your name cannot contain numbers', 'error')
	# if birthday is not in the past
	elif not checkBirthday(session['bday']):
		flash("You can't be born in the future!", 'error')
	# if password is less than 8 characters
	elif len(session['password'])<8:
		flash('Password must but more than 8 characters', 'error')
	# if password doesn't match with confirmed password
	elif session['password']!=cpw: 
		flash("Confirmation password does not match password", 'error')
	# if password doesn't contain at least 1 uppercase and 1 digit
	elif not checkPW(session['password']): 
		flash("Password must contain at least 1 uppercase and 1 numeric value", 'error')
	else: # if no errors
		flash('Success!', 'success')
	return redirect('/') # redirects back to root
app.run(debug=True)