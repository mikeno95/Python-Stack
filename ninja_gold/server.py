from flask import Flask, request, redirect, render_template, session
import random 
import datetime

app = Flask(__name__)
app.secret_key = 'secret123abc'

@app.route('/')
def index():
	# when user goes to page for first time, variables in session are set empty variable
	if 'gold' not in session: 
		session['gold'] = 0 
	if 'building_name' not in session: 
		session['building_name'] = ""
	if 'gold_list' not in session: 
		session['gold_list'] = []
	if 'gold_add' not in session: 
		session['gold_add']=0
	return render_template('index.html', gold = session['gold'], gold_add=session['gold_add'],gold_list=session['gold_list'])

@app.route('/process_money', methods=['POST'])
def process_money():
	if request.form['building'] == 'farm': # if button for farm is clicked
		session['gold_add']=random.randint(10,20) # set session 'gold_add' to a random integer between 10-20
	elif request.form['building'] == 'cave': # if button for cave is clicked 
		session['gold_add']=random.randint(5,10) # set session 'gold_add' to a random integer between 5-10
	elif request.form['building'] == 'house': # if button for house is clicked
		session['gold_add']=random.randint(2,5) # set session 'gold_add' to a random integer between 2-5
	elif request.form['building'] == 'casino': # if button for casino is clicked
		session['gold_add']=random.randrange(-50,50) # set session 'gold_add' to a random integer between -50 and 50
	
	session['gold']+=session['gold_add'] # add session 'gold_add' to session 'gold'
	session['building_name']=request.form['building'] # set session 'building_name' to the value of the building submit inputs

	if session['gold_add']<0: # if session_gold add is negative (lost money)
		# set string to: 
		string="Entered a casino and lost {} golds...ouch...{}	".format(session['gold_add'],datetime.datetime.now())
		# and color fo the css to 
		color='color:red;'
	else: # else (add is positive)
		string = "Earned {} golds from the {}!	{}".format(session['gold_add'],session['building_name'],datetime.datetime.now())
		color='color:green;'
	session['gold_list'].insert(0,{'color':color, 'string':string}) # create a dictionary for color and string and insert that into the beginning of session gold_list
	# insert at beginning (index 0) for scroll (print the string in the HTML before rather than after the previous string)
	return redirect('/') # redirects back to the '/' page
app.run(debug=True)
