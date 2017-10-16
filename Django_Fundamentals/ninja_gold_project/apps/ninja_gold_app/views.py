from django.shortcuts import render, redirect, HttpResponse
import random
from time import gmtime, strftime
# Create your views here.
def index(request):
	if 'gold' not in request.session: 
		request.session['gold'] = 0
	if 'building_name' not in request.session: 
		request.session['building_name'] = ""
	if 'gold_list' not in request.session:
		request.session['gold_list'] = []
	if 'gold_add' not in request.session: 
		request.session['gold_add'] = 0
	return render(request,'ninja_gold_app/index.html')

def process(request):
	if request.POST['building'] == 'farm':
		request.session['gold_add'] = random.randint(10,20)
	elif request.POST['building'] == 'cave':
		request.session['gold_add'] = random.randint(5,10)
	elif request.POST['building'] == 'house':
		request.session['gold_add'] = random.randint(2,5)
	elif request.POST['building'] == 'casino':
		request.session['gold_add'] = random.randint(-50,50)

	request.session['gold']+=request.session['gold_add']
	request.session['building_name'] = request.POST['building']
	current_time = strftime("(%Y/%m/%d %I:%M %p)", gmtime())
	if request.session['gold_add']<0:
		string = "Entered a casino and lost {} golds...ouch...{}	".format(request.session['gold_add'], current_time)
		str_color = "red"
	else: 
		string = "Earned {} golds from the {}!	{}".format(request.session['gold_add'],request.session['building_name'], current_time)
		str_color = "green"
	request.session['gold_list'].insert(0, {'string':string, 'str_color':str_color})
	return redirect('/')