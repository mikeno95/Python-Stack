from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'survey_app/index.html')

def process(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']

	if len(request.session['name'])<1:
		messages.warning(request, 'Please enter your name')
	elif request.session['location'] == 'Location':
		messages.warning(request, 'Please select your dojo location')
	elif request.session['language'] == 'Language':
		messages.warning(request, 'Please select your favorite language')
	elif len(request.session['comment'])>120:
		messages.warning(request, 'Your comment must be less than 120 characters')
	else:
		return redirect('/results')
	return redirect('/')

def results(request):
	try: 
		request.session['count']+=1
	except: 
		request.session['count']=1
	return render(request,'survey_app/results.html')

def restart(request):
	del request.session['name']
	del request.session['location'] 
	del request.session['language'] 
	del request.session['comment']
	return redirect('/')