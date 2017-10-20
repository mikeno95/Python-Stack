from django.shortcuts import render, HttpResponse, redirect
from .models import Users
from django.contrib import messages
import bcrypt
from django.contrib.auth.hashers import check_password
# Create your views here.
def emailChecker(m):
	for user in Users.objects.all():
		if m == user.email:
			return True
	return False

def index(request):
	return render(request, 'login_app/index.html')

def create(request):
	errors = Users.objects.basic_validator(request.POST)
	if len(errors):
		for error in errors.itervalues():
			messages.error(request,error)
		return redirect('/')
	elif emailChecker(request.POST['email']): 
		messages.error(request, "You cannot have multiple accounts with the same email")
		return redirect('/')
	else: 
		email = request.POST['email']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		# password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		new_user = Users.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
		messages.success(request, "Successfully registered")
		request.session['id'] = new_user.id
		return redirect('/success')

def login(request):
	email = request.POST['email']
	password = request.POST['password']
	login_user = Users.objects.get(email=email)
	input_password = login_user.password
	if bcrypt.checkpw(password.encode(), input_password.encode()):
		messages.success(request, "Successfully logged in")
		request.session['id'] = login_user.id
		return redirect('/success')
	else: 
		messages.error(request, "Incorrect Password")
		return ('/')


def success(request):
	context = {
		'user': Users.objects.get(id=request.session['id'])
	}
	return render(request,'login_app/success.html', context)