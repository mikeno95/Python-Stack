# users_app views.py
from django.shortcuts import render, redirect, HttpResponse 

# Create your views here.
def root(request):
	return redirect('/blogs') # main root redirects to the index page of the blog 
	# return render(request,'blogs_app/index.html')

def index(request): 
	return render(request,'users_app/index.html')

def new(request):
	return redirect('/users/register')

def login(request):
	return render(request,'users_app/login.html')

def register(request):
	return render(request, 'users_app/register.html')