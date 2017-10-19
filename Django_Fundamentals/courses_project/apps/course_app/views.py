from django.shortcuts import render, HttpResponse, redirect
from .models import Courses
from django.contrib import messages
# Create your views here.
def index(request):
	context = {
		'courses': Courses.objects.all(),
	}
	return render(request, 'course_app/index.html', context)

def create(request):
	errors = Courses.objects.basic_validator(request.POST)
	if len(errors):
		for error in errors.itervalues():
			messages.error(request, error)
	else: 
		course_name = request.POST['course_name']
		desc = request.POST['desc']
		Courses.objects.create(name=course_name , desc=desc)
	return redirect('/')

def destroy(request, id):
	context = {
		'course': Courses.objects.get(id=id),
	}
	return render(request, 'course_app/destroy.html', context)

def bye(request, id):
	Courses.objects.get(id=id).delete()
	return redirect('/')