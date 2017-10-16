from django.shortcuts import render, redirect, HttpResponse
import random
from time import gmtime, strftime
# Create your views here.
def index(request):
	if 'gold_count' not in request.session: 
		request.session['gold_count'] = 0
	if 'build_name' not in request.session: 
		request.session['build_name'] = ""
	if 'gold_update' not in request.session: 
		request.session['gold_update'] = []
	if 'add_gold' not in request.session: 
		request.session['add_gold'] = 0
	return render(request,'bonus_gold_app/index.html')

def process_farm(request):
	request.session['add_gold'] = random.randint(10,20)
	request.session['build_name'] = 'farm'
	return redirect('/bonus/process')

def process_cave(request):
	request.session['add_gold'] = random.randint(5,10)
	request.session['build_name'] = 'cave'
	return redirect('/bonus/process')

def process_house(request):
	request.session['add_gold'] = random.randint(2,5)
	request.session['build_name'] = 'house'
	return redirect('/bonus/process')

def process_casino(request):
	request.session['add_gold'] = random.randint(-50,50)
	request.session['build_name'] = 'casino'
	return redirect('/bonus/process')

def process(request):
	request.session['gold_count']+=request.session['add_gold']
	current_time = strftime("(%Y/%m/%d %I:%M %p)", gmtime())
	if request.session['add_gold']<0:
		string = "Entered a casino and lost {} golds...ouch...	{}".format(request.session['add_gold'], current_time)
		str_color = "red"
	else: 
		string = "Earned {} golds from the {}!	{}".format(request.session['add_gold'],request.session['build_name'], current_time)
		str_color = "green"
	request.session['gold_update'].insert(0, {'string':string, 'str_color':str_color})
	return redirect('/bonus')
