from flask import Flask, redirect, session, request, render_template
import random

# create a site that when a user loads it creates a random number between 1-100 
# stores the number in a session 
# allow the user to guess at the number and tell them when they are too high or too low

app = Flask(__name__)
app.secret_key='secret123'

@app.route('/')
def index():
	if 'guess_number' not in session: 
		session['guess_number'] = None
	if 'random_number' not in session: 
		session['random_number'] = random.randrange(1,100)
	return render_template('index.html', guess_number=session['guess_number'], random_number=session['random_number'])

@app.route('/results', methods=['POST'])
def result():
	session['guess_number']=int(request.form['guess'])
	return redirect('/')

@app.route('/finish')
def finish():
	session['guess_number']= None
	session['random_number'] = random.randrange(1,100)
	return redirect('/')

app.run(debug=True)
