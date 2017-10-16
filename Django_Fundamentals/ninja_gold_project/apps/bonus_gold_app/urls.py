from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_farm$', views.process_farm),
    url(r'^process_cave$', views.process_cave),
	url(r'^process_house$', views.process_house),
	url(r'^process_casino$', views.process_casino),
	url(r'^process$', views.process),
]