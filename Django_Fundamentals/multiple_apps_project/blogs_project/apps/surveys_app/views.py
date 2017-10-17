# surveys_app views.py
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'surveys_app/index.html')

def new(request): 
	return render(request, 'surveys_app/new.html')