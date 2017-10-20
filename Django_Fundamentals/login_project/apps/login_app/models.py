from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
# Create your models here.


def checkString(word):
	for i in word: 
		if i.isdigit():
			return True
	return False

class UserManager(models.Manager):
	def basic_validator(self, postData): 
		errors = {}
		if len(postData['first_name'])<2:
			errors['first_name'] = "Please enter your first name"
		if len(postData['last_name'])<2:
			errors['last_name'] = "Please enter your last name"
		if checkString(postData['first_name']):
			errors['first_name'] = "Please enter valid first name"
		if checkString(postData['last_name']):
			errors['last_name'] = "Please enter valid last name"
		if postData['password'] != postData['cpassword']:
			errors['password'] = "Your password didn't match. Try again."
		try: 
			validate_email(postData['email'])
		except ValidationError as e: 
			errors['email'] = "Please enter a valid email"
		return errors

class Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()


