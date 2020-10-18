from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
	return render(request, 'generator/home.html')


def password(request):
	
	charc = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		charc.extend(list('ABCDEFGHIJKLMONPQRSTUVWXYZ'))

	if request.GET.get('numbers'):
		charc.extend(list('1234567890'))

	if request.GET.get('special'):
		charc.extend(list('!@#$%^&*()_=-+?><{/}[]]'))



	length = int(request.GET.get('length',12))

	password = ''

	for x in range(length):
		password += random.choice(charc)

	return render(request, 'generator/password.html', {'password':password})

def about(request):
	return render(request, 'generator/about.html')