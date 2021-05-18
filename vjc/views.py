from django.shortcuts import render
from django.http import HttpResponse
from .models import Events

def home(request):
	
	context = {
		'events': Events.objects.all()
	}


	return render(request, 'vjc/tmp.html', context)


def about(request):
	return render(request, 'vjc/about.html')

def login(request):
	return render(request, 'users/register.html')



# def log_reg (request):
	



# Create your views here.