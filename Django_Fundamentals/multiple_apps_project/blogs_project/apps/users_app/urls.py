# users_app urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.root),
	url(r'^users$', views.index),
	url(r'^users/new$', views.new),
	url(r'^login$', views.login),
	url(r'^register$', views.register),  
]
