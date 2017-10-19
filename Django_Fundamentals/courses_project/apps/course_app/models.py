from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['course_name'])<5:
			errors['course_name'] = "Course name must be more than 5 characters"
		if len(postData['desc'])<15:
			errors['desc'] = "Description must be more than 15 characters"
		return errors;

class Courses(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = CourseManager()
