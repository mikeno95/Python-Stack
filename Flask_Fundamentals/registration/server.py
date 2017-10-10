from flask import Flask, render_template, redirect, session, request, flash
import re
from datetime import date, datetime

app = Flask(__name__)

app.secret_key = "shhhhhhhhh. it's a secret"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def checkString(string): 
	for i in string: 
		if i.isdigit():
			return False
	return True

def checkPW(password):
	count_int = 0
	count_up = 0
	for i in password:
		if i.isupper(): 
			count_up+=1
		elif i.isdigit():
			count_int+=1
	if count_int>0 and count_up>0:
		return True
	return False
	
def checkBirthday(strbday):
	bday = datetime.strptime(strbday, '%Y-%m-%d').date()
	today = date.today()
	if bday>today: 
		return False
	return True

@app.route('/')
def index():
	if 'email' not in session: 
		session['email'] = ''
	if 'first_name' not in session:
		session['first_name'] = ''
	if 'last_name' not in session: 
		session['last_name'] = ''
	if 'password' not in session: 
		session['password'] = ''
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def result():
	session['email'] = request.form['email']
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['bday'] = request.form['bday']
	session['password'] = request.form['psw']
	cpw = request.form['cpsw']

	if len(session['email']) < 1 or len(session['first_name'])<1 or len(session['last_name'])<1:
		flash('All fields are required and must not be blank.', 'error') 
	elif not EMAIL_REGEX.match(session['email']):
		flash('Please enter a valid email', 'error')
	elif not checkString(session['first_name']) or not checkString(session['last_name']): 
		flash('Your name cannot contain numbers', 'error')
	elif not checkBirthday(session['bday']):
		flash("You can't be born in the future!", 'error')
	elif len(session['password'])<8:
		flash('Password must but more than 8 characters', 'error')
	elif session['password']!=cpw: 
		flash("Confirmation password does not match password", 'error')
	elif not checkPW(session['password']): 
		flash("Password must contain at least 1 uppercase and 1 numberic value", 'error')
	else:
		flash('Success!', 'success')
	return redirect('/')
app.run(debug=True)