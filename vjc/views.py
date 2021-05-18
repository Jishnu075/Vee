from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	# return HttpResponse('<h1>HOME</h1>')

	return render(request, 'vjc/tmp.html')

def about(request):
	return HttpResponse('Sample about page')
	# context = {
	# 	"first_name" : "Axew",
	# }
	# context['first_name'] =  "Axew"
	# context['mid_name'] =  "Axew 1"
	# context['last_name'] =  "Axew 2"
	# return render(request, 'vjc/about.html',context)

# def log_reg (request):
	



# Create your views here.