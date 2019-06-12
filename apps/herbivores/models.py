# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ReservationManager(models.Manager):
	def validate_reservation(request, postData):
		errors = {}

		#validate firstname
		if len(postData['firstname']) < 3:
			errors['firstname'] = "First name must be longer than 3 characters"

		#validate lastname
		if len(postData['lastname']) < 3:
			errors['lastname'] = "Last name must be longer than 3 characters"

		if len(postData['email']) < 3:
			errors['email'] = "Last name must be longer than 3 characters"

		if len(postData['phone']) < 3:
			errors['phone'] = "Phone number must be at least 10 digits"

		return errors

class FeedbackManager(models.Manager):
	def validate_feedback(request, postData):
		errors = {}

		if len(postData['feedback']) < 10:
			errors['feedback'] = "Not enough characters in this message"

		return errors

class QueryManager(models.Manager):
	def validate_query(request, postData):
		errors = {}

		if len(postData['firstname']) < 3:
			errors['firstname'] = "First name must be longer than 3 characters"

		if len(postData['lastname']) < 3:
			errors['lastname'] = "Last name must be longer than 3 characters"

		if len(postData['email']) < 3:
			errors['email'] = "Last name must be longer than 3 characters"

		if len(postData['subject']) < 5:
			errors['subject'] = "Subject must be longer than 5 characters"

		if len(postData['message']) < 10:
			errors['message'] = "Message must be longer than 10 characters"

		return errors


class Reservation(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	email = models.CharField(max_length=30)
	phone = models.IntegerField(default=0)
	party = models.IntegerField(default=0)
	date = models.DateTimeField(auto_now=False, auto_now_add=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ReservationManager()

class Feedback(models.Model):
	message = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = FeedbackManager()

class Query(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	email = models.CharField(max_length=30)
	subject = models.CharField(max_length=30)
	message = models.CharField(max_length=150)
	objects = QueryManager()
