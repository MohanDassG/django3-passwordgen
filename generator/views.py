from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
	return render(request, 'generator/home.html')

def password(request):
	cha = list('abcdefghijklmnopqrstuvwxyz')
	if request.GET.get('uppercase'):
		cha.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special'):
		cha.extend(list('!@#$%^&*()'))
	if request.GET.get('numbers'):
		cha.extend(list('1234567890'))
	length = int(request.GET.get('length',12))
	thepassword = ''
	for x in range(length):
		thepassword+=random.choice(cha)
	return render(request, 'generator/password.html', {'password':thepassword})
def about(request):
	return render(request, 'generator/about.html')