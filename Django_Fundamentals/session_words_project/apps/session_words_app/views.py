from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index(request):
	if 'word_list' not in request.session:
		request.session['word_list']=[]
	return render(request,'session_words_app/index.html')

def add_word(request):
	word=request.POST['new_word']
	if not len(word):
		messages.warning(request, 'Please enter a word')
		return redirect('/')

	if 'color' in request.POST:
		color=request.POST['color']	
	else:
		color = False
		messages.warning(request, 'Please select a color')
		return redirect('/')

	if 'big' in request.POST:
		big = request.POST['big']
	else:
		big = False

	request.session['time'] = strftime("%I:%M:%S%p, %B %dth %Y", gmtime())
	request.session['word_list'].append({'word':word, 'w_color':color, 'big':big, 'time': request.session['time']})
	return redirect('/')

def clear(request):
	request.session['word_list']=[]
	return redirect('/')