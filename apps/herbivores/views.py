# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def home(request):
	return render(request, 'herbivores/homepage.html')

def menu(request):
	return render(request, 'herbivores/menu.html')

def breakfast_menu(request):
	return render(request, 'herbivores/breakfast_menu.html')

def lunch_menu(request):
	return render(request, 'herbivores/lunch_menu.html')

def dinner_menu(request):
	return render(request, 'herbivores/dinner_menu.html')

def dessert_menu(request):
	return render(request, 'herbivores/dessert_menu.html')

def reservations(request):
	return render(request, 'herbivores/reservations.html')

def coffee(request):
	return render(request, 'herbivores/coffeetea.html')

def drinks(request):
	return render(request, 'herbivores/drinks.html')

def process_reservation(request):
	errors = Reservation.objects.validate_reservation(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error)
		return redirect('/reservations')

	else:
		firstname = request.POST['first_name']
		lastname = request.POST['last_name']
		email = request.POST['email']
		phone = request.POST['phone']
		party = request.POST['party']
		date = request.POST['date']
		reservation = Reservation.objects.create(firstname=firstname, lastname=lastname, email=email, phone=phone, party=party, date=date)
		print "Reservation created"
		print "first Name:", firstname
		print "Last Name:", lastname
		print "email:", email
		print "party:", party
		print "date:", date
		return redirect('/')

def team(request):
	return render(request, 'herbivores/team.html')

def contact(request):
	return render(request, 'herbivores/contact.html')


