from django.shortcuts import render, HttpResponse, redirect
from .models import Courses, Descriptions, Comments
from django.contrib import messages
# Create your views here.
def index(request):
	context = {
		'courses': Courses.objects.all(),
	}
	return render(request, 'bonus_app/index.html', context)

def create(request):
	course_errors = Courses.objects.basic_validator(request.POST)
	desc_errors = Descriptions.objects.basic_validator(request.POST)
	if len(course_errors):
		for course_error in course_errors.itervalues():
			messages.error(request, course_error)
	elif len(desc_errors): 
		for desc_error in desc_errors.itervalues():
			messages.error(request, desc_error)
	else: 
		course_name = request.POST['course_name']
		desc = request.POST['desc']
		new_course = Courses.objects.create(name=course_name)
		Descriptions.objects.create(desc=desc, course=new_course)
	return redirect('/bonus')

def show(request,id):
	context = {
		'course':Courses.objects.get(id=id),
	}
	return render(request, 'bonus_app/show.html', context)

def comment(request, id):
	comment = request.POST['comment']
	new_comment = Comments.objects.create(comment=comment, course=Courses.objects.get(id=id))
	return redirect('/bonus/course/'+str(id))

def destroy(request, id):
	context = {
		'course': Courses.objects.get(id=id),
	}
	return render(request, 'bonus_app/destroy.html', context)

def bye(request, id):
	Courses.objects.get(id=id).delete()
	return redirect('/bonus')