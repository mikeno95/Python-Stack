from django.shortcuts import render, HttpResponse, redirect
from .models import User # import model
from django.contrib import messages # import to use flash messages

# Create your views here.
def index(request):
	context = {
		'users':User.objects.all(),
	}
	return render(request, 'semi_users_app/index.html', context) # renders the page with the table

def new(request):
	return render(request, 'semi_users_app/new.html') # renders the page with the form to add a new user

def create(request): # post route to create new user from the client's input
	errors = User.objects.basic_validator(request.POST) # checks errors and validation
	if len(errors): # if there are errors
		for error in errors.itervalues():
			messages.error(request, error) # flash messages for errors
		return redirect('/users/new') # redirects back to the page with the form
	else: # if there are no errors
		first_name = request.POST['first_name'] # takes in all the input
		last_name = request.POST['last_name']
		email = request.POST['email']
		User.objects.create(first_name=first_name, last_name=last_name, email=email) # creates new user
		return redirect('/users/' + str(User.objects.last())) # redirects to the 'show' page for that created user

def show(request, id): # page that shows the selected user
	context = {
		'user':User.objects.get(id=id), # Get user with id that was passed
	}
	return render(request,'semi_users_app/show.html', context) # render the 'show' page

def edit(request, id): # page that shows the form to edit selected user
	context = {
		'user':User.objects.get(id=id), # get usr with id 
	}
	return render(request,'semi_users_app/edit.html', context) # renders edit page

def update(request, id): # post root from edit page the updates the user's info
	errors = User.objects.basic_validator(request.POST) # validates input
	if len(errors): 
		for error in errors.itervalues():
			messages.error(request, error)
		return redirect('/users/'+str(id)+'/edit') # if there are errors, redirects back to the edit page
	else: # if no error
		user = User.objects.get(id=id)
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email'] # set info to the user's inputs
		user.save() # save the change
		return redirect('/users/'+str(id)) # redirect back to the show page

def check(request,id): # render page that asks if they really want to delete that user
	context = {
		'user':User.objects.get(id=id),
	}
	return render(request, 'semi_users_app/check.html', context)
def destroy(request,id): # if client really wants to delete user, redirects to destroy post root
	User.objects.get(id=id).delete() # deletes user with selected id
	return redirect('/users') # redirects back to root

	