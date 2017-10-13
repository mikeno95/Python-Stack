from django.shortcuts import render, HttpResponse, redirect 

def index(request): 
	response = 'placeholder to later display all the list of blogs'
	return HttpResponse(response) # returns the string

def new(request):
	response = 'placeholder to display a new form to create a new blog'
	return HttpResponse(response) # returns the string 

def create(request): 
	return redirect('/') # redirects back to main roote

def show(request, number): # takes in request and variable number, which is from <number>
	response = 'placeholder to display blog ', number
	return HttpResponse(response)

def edit(request,number): # takes in request and variable number, which is from <number>
	response =  'placeholder to edit blog ', number
	return HttpResponse(response)

def destroy(request,number): 
	return redirect('/') # redirects back to main root