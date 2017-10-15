from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request): 
	try:
		request.session['count'] += 1
	except:
		request.session['count']=0
	return render(request, 'random_app/index.html')

def generate(request):
	request.session['random'] = get_random_string(length=14)
	return redirect('/random_word/')

def restart(request):
	del request.session['random']
	del request.session['count']
	return redirect('/random_word')