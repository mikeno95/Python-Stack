from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class UserManager(models.Manager): # class UserManager for validation (validates client's inputs)
	def basic_validator(self, postData):
		errors = {} # stores all the error messages in a dictionary
		if len(postData['last_name'])<1: # if last_name is less than 1 character
			errors['last_name']="Please enter your last name"
		if len(postData['first_name'])<1: # if first_name is less than 1 character
			errors['first_name']="Please enter your first name"
		try: 
			validate_email(postData['email']) # validate email
		except ValidationError as e: # if validate_email, throws an error:
			errors['email']="Please enter a valid email address"
		return errors; # returns the error dictionary

class User(models.Model):
	# column names for User
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# set variable 'objects' as UserManager for validation
	objects = UserManager()
# Create your models here.
