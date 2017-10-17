# blogs_app urls.py
from django.conf.urls import url # gives us access to function URL 
from . import views # explicitly import views.py in the current folder 
# from . means 'from current directory'

urlpatterns = [
	url(r'^$', views.index), # url() is similar to @app.route in flask 
	url(r'^new$', views.new), # for /new, uses the new function from view.py
	url(r'^create$', views.create), # for /create, uses the create function from view.py
	url(r'^(?P<number>\d+)$', views.show), #/{{number}}, uses the show function from view.py
	url(r'^(?P<number>\d+)/edit$', views.edit), # /{{number}}/edits uses the edit function from view.py
	url(r'^(?P<number>\d+)/delete$', views.destroy), # /{{number}}/delete, uses the destroy function from view.py
]

